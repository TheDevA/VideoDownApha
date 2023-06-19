import yt_dlp
import json
import sys
import re

# URL = 'https://www.youtube.com/watch?v=X4KNqjF34E4'

# info = ""

# ydl_opts = {'format': "all"}
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#   info0 = ydl.extract_info(URL, download=False)

#   # with open('inf.txt', 'w') as f:
#   #   f.write(str(info0))

#   for fmt in info0["formats"]:
#     print("extanction:"+fmt["ext"]+" format: "+ fmt["format"])
#   info = info0["formats"][0]["ext"]

#   # print(info)


def main():
  args = sys.argv
  URL = args[1]
  ORDER = args[2]
  if ORDER == "INFO":
    formats = []
    title = ""
    id = ""
    duration = ""
    uploader = ""
    with yt_dlp.YoutubeDL({"quiet":True}) as ydl:
      info0 = ydl.extract_info(URL, download=False)
      title = info0['title']
      id = info0["id"]
      thumbnail = info0["thumbnail"]
      duration = info0["duration"]
      uploader = info0["uploader"]
      for fmt in info0["formats"]:
        format = fmt["format"]
        formats.append(format)

    DATA = {
      "title": title,
      "id": id,
      "channel": uploader,
      "thumbnail": thumbnail,
      "duration": round(duration / 60, 2),
      "formats": formats
    }
    print(json.dumps(DATA))


if __name__ == "__main__":
  main()
