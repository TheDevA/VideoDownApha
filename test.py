import json
DATA = {
      "title": "title",
      "id": "id",
      "channel": "uploader",
      "thumbnail": "thumbnail",
      "duration": "round(duration / 60, 2)",
      "formats": "formats"
    }
print(json.dumps(DATA))