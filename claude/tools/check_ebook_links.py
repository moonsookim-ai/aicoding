"""『클로드 완전정복 100단계』 원고에 적힌 바깥 주소가 아직 열리는지 확인한다.

새 판을 내기 전에 돌린다. 원고(docs/ebook/*.md, 곁 파일 포함)에서 http(s) 주소를 모아
하나씩 열어 보고, 열리지 않는 주소와 다른 곳으로 옮겨 간 주소를 알려 준다.

  python3 tools/check_ebook_links.py            # 전부 확인
  python3 tools/check_ebook_links.py --quiet    # 문제 있는 주소만

끝 코드: 열리지 않는 주소가 있으면 1. 옮겨 간 주소는 알려만 준다.
GitHub·일부 사이트는 로봇의 요청을 막아 403을 돌려주기도 한다. 그런 주소는 "막힘"으로 따로 적으니
브라우저로 한 번 열어 본다.
"""
import concurrent.futures
import glob
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "book")
URL_RE = re.compile(r"https?://[^\s<>()\[\]\"'`|]+")
UA = "Mozilla/5.0 (link check for ceoai.kr ebook)"


def collect():
    found = {}
    files = glob.glob(os.path.join(SRC, "*.md")) + glob.glob(os.path.join(SRC, "*", "*.md")) + glob.glob(os.path.join(SRC, "*.json"))
    for path in sorted(files):
        with open(path, encoding="utf-8") as f:
            text = f.read()
        if path.endswith(".json"):
            text = json.dumps(json.loads(text), ensure_ascii=False)
        for n, line in enumerate(text.splitlines(), 1):
            for u in URL_RE.findall(line):
                u = u.rstrip(".,;:·」』)")
                found.setdefault(u, []).append("%s:%d" % (os.path.relpath(path, ROOT), n))
    return found


def probe(url):
    url = urllib.parse.quote(url, safe=":/?#[]@!$&'()*+,;=%~")  # 한글 파일 이름이 든 주소
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                final = r.geturl()
                return r.status, (final if urllib.parse.unquote(final).rstrip("/") != urllib.parse.unquote(url).rstrip("/") else "")
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (403, 404, 405, 429, 501):
                continue
            return e.code, ""
        except Exception as e:  # noqa: BLE001  연결 실패·시간 초과도 결과로 적는다
            if method == "HEAD":
                continue
            return 0, type(e).__name__
    return 0, ""


def main():
    quiet = "--quiet" in sys.argv
    found = collect()
    bad, moved, blocked = [], [], []
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
        for url, (code, extra) in zip(found, pool.map(probe, found)):
            where = ", ".join(found[url][:3]) + (" 외 %d곳" % (len(found[url]) - 3) if len(found[url]) > 3 else "")
            if code in (401, 403, 429):
                blocked.append((url, code, where))
            elif code == 405:  # 글 보내기(POST)만 받는 API 주소 - 살아 있다
                pass
            elif not (200 <= code < 400):
                bad.append((url, code or extra, where))
            elif extra:
                moved.append((url, extra, where))
            elif not quiet:
                print("OK   ", url)
    for title, rows in (("열리지 않음", bad), ("막힘(브라우저로 확인)", blocked), ("옮겨 감", moved)):
        if rows:
            print("\n## %s %d개" % (title, len(rows)))
            for url, info, where in rows:
                print("- %s  [%s]  %s" % (url, info, where))
    print("\n주소 %d개 · 열리지 않음 %d · 막힘 %d · 옮겨 감 %d" % (len(found), len(bad), len(blocked), len(moved)))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
