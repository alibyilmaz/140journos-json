from youtube_statistics import YTstats

API_KEY = "your-api-key" #get from google console
channel_id = "UCO-_F5ZEUhy0oKrSa69DLMw" #get channel id 

yt = YTstats(API_KEY, channel_id)
yt.get_channel_statistics()
yt.get_channel_video_data()
yt.dump()
#yt.get_channel_video_data()
