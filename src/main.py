import requests

TOKEN = '10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c'


class VkUser:
    url = 'https://api.vk.com/method/'
    def __init__(self, user_id, version='5.199'):
        self.user_id = user_id
        self.version = version
        self.params = {
            'access_token': TOKEN,
            'v': version
        }

    def get_friends(self):
        friends_url = self.url + 'friends.get'
        friends_params = {
            'user_id': self.user_id
        }
        response = requests.get(friends_url, params={**self.params, **friends_params})
        return response.json()['response']['items']

    def __str__(self):
        return f'https://vk.com/id{self.user_id}'

    def __and__(self, other):
        return [VkUser(common_friend_id) for common_friend_id in set(self.get_friends()) & set(other.get_friends())]


def solution():
    user_id1 = input()
    user1 = VkUser(user_id1)
    print(user1)
    print(user1.get_friends())

    user_id2 = input()
    user2 = VkUser(user_id2)
    print(user2)
    print('common_friends:')
    common_friends = user1 & user2
    for friend in common_friends:
        print(friend)


if __name__ == '__main__':
    solution()
