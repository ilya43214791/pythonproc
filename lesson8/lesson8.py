from abc import ABC, abstractmethod


class SocialChannel(ABC):
    def __init__(self, type: str, followers: int):
        self.type = type
        self.followers = followers

    @abstractmethod
    def post_message(self, message: str):
        pass


class YouTubeChannel(SocialChannel):
    def post_message(self, message: str):
        print(f"Posting to YouTube: {message}")


class FacebookChannel(SocialChannel):
    def post_message(self, message: str):
        print(f"Posting to Facebook: {message}")


class TwitterChannel(SocialChannel):
    def post_message(self, message: str):
        print(f"Posting to Twitter: {message}")


class Post:
    def __init__(self, message: str, timestamp: int):
        self.message = message
        self.timestamp = timestamp


def post_a_message(channel: SocialChannel, message: str) -> None:
    channel.post_message(message)


youtube_channel = YouTubeChannel("youtube", 1000)
facebook_channel = FacebookChannel("facebook", 500)
twitter_channel = TwitterChannel("twitter", 200)

channels = [youtube_channel, facebook_channel, twitter_channel]

post1 = Post("Hello YouTube!", 10)
post2 = Post("Hello Facebook!", 20)
post3 = Post("Hello Twitter!", 30)

posts = [post1, post2, post3]
