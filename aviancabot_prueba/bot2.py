from TwitterAPI import TwitterAPI
api = TwitterAPI('DwDK8z8hhd1VBWToqKkEWraeN', 'QfFQ8HNGdFWZYphVu62Bsx6JtDA72FPA1onXZkYa5WQxJexi2V', '782779396675477504-q8wnkKCQVcWVVJ2IqLxMxWGTi7aYWJD', 'WHYKEgHORfhEfHD4LgPM4LDgCbtEbUJTKwZCn8GQOQp1x')
r = api.request('search/tweets', {'q':'pilotos'})
for item in r:
        print (item['text'] + item['id_str'] + item['created_at'] + item['user']['id_str'] + item['user']['screen_name'] )
        print (int(item['user']['followers_count'] + item['retweet_count'] + item['favorite_count'])) 