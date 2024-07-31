import requests
import json

# Define the URL
url = 'https://gql.tokopedia.com/graphql/PDPGetReviewImageQuery'

# Define the headers
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://www.tokopedia.com',
    'referer': 'https://www.tokopedia.com/racoonofficial/racoon-arap-spray-anti-rayap-obat-anti-rayap-500ml?src=topads',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-source': 'tokopedia-lite',
    'x-tkpd-lite-service': 'zeus',
    'x-version': '505dab6',
    'cookie': '_UUID_NONLOGIN_=bb1e65d922ee6719dd56e233ad422759; DID=c025fdfc785237b302c2e39a8991b55ee51fda592f78aa608983ca0f0af52ae4abce170c7afc5994eaa50c56ed46cd8f; DID_JS=YzAyNWZkZmM3ODUyMzdiMzAyYzJlMzlhODk5MWI1NWVlNTFmZGE1OTJmNzhhYTYwODk4M2NhMGYwYWY1MmFlNGFiY2UxNzBjN2FmYzU5OTRlYWE1MGM1NmVkNDZjZDhm47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=; _UUID_CAS_=a85b18ad-8d23-4152-aaf9-beeedbca2895; hfv_banner=true; _CASE_=7c25634e63253d353530332b25664e63253d372b256b656b253d254d666c66757366275772746673252b25644e63253d3630312b256b686960253d25252b256b6673253d25252b25774468253d25252b25704e63253d36353536373430322b25744e63253d36363234373230342b2574537e7762253d25356f252b25706f74253d255c7c5b25746275716e646258737e77625b253d5b25356f5b252b5b25706675626f68727462586e635b253d36353536373430327a2b7c5b25746275716e646258737e77625b253d5b2536326a5b252b5b25706675626f68727462586e635b253d377a5a252b256b527763253d25353735332a37352a35355336343d343e3d323f2c37303d3737257a; _gcl_au=1.1.78240494.1717764429; _tt_enable_cookie=1; _ttp=gm8U34RMiN4AbxcANky-VcVCVnX; _gid=GA1.2.1292334056.1722334672; _SID_Tokopedia_=KYoifjWhkUEf9nBfs5ZpfPToz76zvm_p43mEKajvZmvidi-8-MyxclkWyvwjVIfKrrCCy9pPwtWaC6bJkNDLApbNG40UKbQvFXfYNJurK3HicmVQfO9j5nsRJWh2vvD0; ak_bmsc=EA0F65DF3A335C79FE0425CB55A562FE~000000000000000000000000000000~YAAQrjwxF8Q5iQGRAQAAdcUlBhihi+/RTagBXJ+zCIgzA+1CAM0QE66Z4AaU4WUhlIT5xaQc+xdqVp64xgB1PLrkzjyhUPQlkTRgozso+QY8L/1cR+GOwLX+3kFORC0QEcOVH2j1tjAmjUyezSVAIZzA0C7/awri/aKfTu775OI/0O16Quvi1qI4VBEcfl9r3YA2J5HVdj3UBkbYYFc2o8spGAZ9qgMEtKbdvZ5ZgU8HamteqFQdhhiIv1KItL/rWAKErut8srP4eoBHDwtodglDQHxHCrjw1c9P5YovxFzQky68MOegV3HizZ2UT9eSZI3S80geMEbc0szI4skiVTVH+qipvGkrfttnJ6r4Atk88z5ZVG8oEPLO6P9KL76scrclFYuUphkFrlipzec5/KRpucxoBLZCBePJJQk+A/+fkdB5/3G9acd8u+zkLkHYErvk+QwM41mR+KGmSLiIEMc=; AMP_TOKEN=%24NOT_FOUND; _abck=3A95EA188B9331B3777EF2A1930B7FB8~0~YAAQyc4tF639OASRAQAA28QpBgxzRhlaHs01MkzbXRQMXWgB/mjWNqAUsElgMWAXXdVRx0LE3yjo1D5oHadQCMkNK5WarMwoEiKEeLPE4OyycEgRzWH0+RXRLwlJZ3pwzfeVXDQ0h2GMDDSQom0MD+BkY9mqyhXuAxrokCt5ZOcPUiSkz4IZGvQZ3vFZjTDkVUC/Abzu8T71FCETDklJetNnsylcveD8RhJCc7uFKrWt3woeZUySTxa/BcIvOVzaTh2KOFTkZFZrNIjXugm6ul/Vy4OUjfjnLjOM24xRcVMHhlcpvFC/sYOBB5qLQAq0O1XBC0qBoT8LDSJuig8OjhvxiS92n5iSdLB8fTvJNrK2Xnxzxgi/gkFizeD44yHGHfbmbJKwRnrb5dka4K4TSP0FihNqGgp2Ame7lZeyvkRdP3otbgcy8OZjPeZ8zGf6Smdfq/qhC3/uRBfuqZDcBdqT6HvyEnw=~-1~-1~-1; _dc_gtm_UA-126956641-6=1; bm_sv=8A730D2DDB7BA2F7A1AF198EF43F655F~YAAQ0c4tF0P8ZgSRAQAAC+YpBhjdSJFSU1GVU5PLHNKRZrEtwor7a3vO8IZifDw56/vYBmiOCc9ni8fVrcSN7VDEnuVd4fFy4+bdfc9KqeJ++xVl74N+1BOGCMUa9HmGpMprBdtvaMVsexhDzujs/uArCZ5Mozcfi00B2VBn4ndaeEJpJblLjdZ3wamF4DUMygEL8p0RIjP21/PQQS2rz8WYTYnksTJk0OV4PWxtkLAwZZCpe/qQqy8SJ++gc4phYgh9~1; bm_sz=5C84219533C8DF43CBE2BDEA4CF8B4B0~YAAQqc4tF95NXwSRAQAA7CUqBhiRqfe016FuAelOJvPMvRi3/REesfFbggJIhE2kr+7jc0UkT3IEHoTLo+Czw8UKLQ2XYOC5yjwhHEU29slpJH98tIWKOBIuJ0OQZ9YoXMXLhdHYxrr8uDADjf08Y321kFqpatJ2ghlqSbzpw8C5DmJA4h0LmewPTsLb2i9ijUw2YVlqYq3prv2EMjrpVJYB98Msc7N1QGc4CkxUARmaWyPyByCWgyGdKgaVvaM7GOkFxc4tRzilifXpjWbDvGg9duJnJZZ7K0zy364+O1XQZFtlxkzo9dPLGe+2lFpbv3SZVk7bsA2pUhsw/qBpnHKRyA1DqL2XNglyenXu7qvdoz0f2hzc+7KUhFwChIX9MQ5C9c1hfYma31XX4IHoxzEdEXERh+KlimmjTUVd5aExOg==~4469046~3360305; ISID=%7B%22www.tokopedia.com%22%3A%22d3d3LnRva29wZWRpYS5jb20%3D.8e1b13e72833f4f929ea618879466be5.1722209669613.1722209669613.1722385313443.6%22%2C%22developer.tokopedia.com%22%3A%22ZGV2ZWxvcGVyLnRva29wZWRpYS5jb20%3D.8fd18e18965a844dd8ea37213d8f159a.1722168288518.1722168288518.1722168290605.1%22%7D; _ga=GA1.2.1307469983.1696555079; _dc_gtm_UA-9801603-1=1; _ga_70947XW48P=GS1.1.1722385022.73.1.1722385328.60.0.0'
}

# Define the data
data = [{
    "operationName":"PDPGetReviewImageQuery",
    "variables":{"productID":"868259638","page":1,"limit":15},
    "query":"query PDPGetReviewImageQuery($page: Int\u0021, $productID: String\u0021, $limit: Int\u0021) {\\n  productrevGetReviewImage(page: $page, productID: $productID, limit: $limit) {\\n    list {\\n      imageID\\n      feedbackID\\n      videoID\\n      __typename\\n    }\\n    detail {\\n      reviews: review {\\n        reviewer: user {\\n          userID\\n          fullName\\n          profilePicture: image\\n          __typename\\n        }\\n        shopID\\n        feedbackID\\n        variantName\\n        reviewText: review\\n        rating\\n        reviewTime: createTimestamp\\n        likeCount: totalLike\\n        badRatingReasonFmt\\n        isLiked\\n        isAnonymous\\n        isReportable\\n        __typename\\n      }\\n      images: image {\\n        attachmentID\\n        description\\n        thumbnailURL\\n        fullsizeURL\\n        feedbackID\\n        __typename\\n      }\\n      video {\\n        attachmentID\\n        url\\n        feedbackID\\n        __typename\\n      }\\n      mediaCount\\n      __typename\\n    }\\n    hasNext\\n    __typename\\n  }\\n}\\n"
}]

# Send the request
response = requests.post(url, headers=headers, json=data)

# Parse the response
json_response = response.json()

# Try to open the existing data file
try:
    with open('tokopedia/detail-products.json', 'r') as f:
        try:
            old_data = json.load(f)
        except json.JSONDecodeError:
            # If the file is empty or contains invalid data, create an empty list
            old_data = []
except FileNotFoundError:
    # If the file does not exist, create an empty list
    old_data = []

# Combine the old and new data
old_data.extend(json_response)

# Write the data back to the file
with open('tokopedia/detail-products.json', 'w') as f:
    json.dump(old_data, f, indent=4)

print("Data has been successfully added to the file detail-products.json")
