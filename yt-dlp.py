import yt_dlp

def download_youtube_video(url, output_path="./downloads"):
    format_str = "bv[height<=720][ext=mp4]+ba[ext=m4a]/b[height<=720][ext=mp4]"

    ydl_opts = {
        "outtmpl": f"{output_path}/%(title)s.%(ext)s",
        "format": format_str
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed successfully!")
    except Exception as e:
        print(f"Error: We tried our best")

if __name__ == "__main__":
    url = input("Enter YouTube video URL: ")
    download_youtube_video(url)
