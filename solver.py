import re, os, sys, json, time, uuid, random, string, base64, requests, tls_client

import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from raducord import *

session = tls_client.Session(
    client_identifier="firefox_120",
    random_tls_extension_order=True
)

def __number__(numb):
    ok = random.random() * 2 + numb
    return round(ok, 16)

r = session.get("https://efw47fpad9.execute-api.us-east-1.amazonaws.com/latest")

pattern = r'window\.gokuProps\s*=\s*\{\s*"key"\s*:\s*"([^"]+)"\s*,\s*"iv"\s*:\s*"([^"]+)"\s*,\s*"context"\s*:\s*"([^"]+)"\s*\};'
match = re.search(pattern, r.text)

key = match.group(1)
iv = match.group(2)
context = match.group(3)

print(f"Context: {context}")
print(f"Key: {key}")
print(f"Iv: {iv}")

r = session.get("https://41bcdd4fb3cb.610cd090.us-east-1.token.awswaf.com/41bcdd4fb3cb/0d21de737ccb/cd77baa6c832/inputs?client=browser")

input = r.json()['challenge']['input']
hmac = r.json()['challenge']['hmac']
region = r.json()['challenge']['region']
challenge_type = r.json()['challenge_type']
difficulty = r.json()['difficulty']

print(f"\n{input}")
print(hmac)
print(region)
print(challenge_type)
print(difficulty)

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'es',
    # 'Content-Length': 'H4cK3dR4Du the best',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Origin': 'https://efw47fpad9.execute-api.us-east-1.amazonaws.com',
    'Priority': 'u=1, i',
    'Referer': 'https://efw47fpad9.execute-api.us-east-1.amazonaws.com/',
    'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}

payload = {
    "challenge": {
        "hmac": hmac,
        "input": input,
        "region": region,
    },
    "checksum": "EC2D2BD3",
    "client": "Browser",
    "domain": "efw47fpad9.execute-api.us-east-1.amazonaws.com",
    "existing_token": None,
    "goku_props": {
        "context": context,
        "iv": iv,
        "key": key,
    },
    "metrics": [
        {"name": "2", "value": __number__(1.7), "unit": "2"},
        {"name": "100", "value": 1, "unit": "2"},
        {"name": "101", "value": 2, "unit": "2"},
        {"name": "102", "value": 1, "unit": "2"},
        {"name": "103", "value": 40, "unit": "2"},
        {"name": "104", "value": 2, "unit": "2"},
        {"name": "105", "value": 0, "unit": "2"},
        {"name": "106", "value": 0, "unit": "2"},
        {"name": "107", "value": 1, "unit": "2"},
        {"name": "108", "value": 0, "unit": "2"},
        {"name": "undefined", "value": 1, "unit": "2"},
        {"name": "110", "value": 1, "unit": "2"},
        {"name": "111", "value": 21, "unit": "2"},
        {"name": "112", "value": 1, "unit": "2"},
        {"name": "undefined", "value": 0, "unit": "2"},
        {"name": "3", "value": __number__(16), "unit": "2"},
        {"name": "7", "value": 0, "unit": "4"},
        {"name": "1", "value": __number__(96), "unit": "2"},
        {"name": "4", "value": 101.5, "unit": "2"},
        {"name": "5", "value": __number__(0.1), "unit": "2"},
        {"name": "6", "value": 198, "unit": "2"},
        {"name": "0", "value": __number__(518), "unit": "2"},
        {"name": "8", "value": 1, "unit": "4"}
    ],
    "signals": [
        {"name": "KramerAndRio", "value": {
            "Present": "iT7BYGRpkjOQzq7O::3454d6468bc7cc819a749175d5bca7e0::f6781cad2a5ff794b51084476aa5a9f85e16460ab43de0dfd7116537786770ac55bb45765cc78238883ab22736bf39224ac2551130352e34f10b69aea5db4a77eccd381879f96a4b5029fffdd2fa183d26806fef7b85919b98f32001a43c33667ca8766bd135078fa6d0f2db6a0e9cf1a840cef1da780875a92db936aa158ad369527766f6f8ecbd19c5bcdc941652dee94c479efd353bf50dee2258d43a84c53f068c12833c3cb2efddc751e88736db5b715bc08d149eead4a2be1bb543ed25b17cbbaf591d44b5fd1073c2a45fe9449320156e313ac6f678249c0cab48c64e3b14bb7e253ec3c203efb0ca1ba892768cafccaf7a89ec7dc07c89daaa0ac6b5fd6e7469b7327fc48ed2424f03901adb90effcbe6a686d2d4863c963dda00f069eac8e3764ee19189dcb223266ec533201405b0b2d470e258478f47266374520cbb86cad33ffd7285356b715fd5122026016781457cf30058e48245df73e2d504a701795db177b1522a252ab1bb2199c2973808e008a3f6547434d8d0487de2b1f4af4b9628259ddd0368b55a799f7bbf22f7ec3066211c25ecbfce2797e2d0f8529fa0cb83a1953d6fee8eef700d9116c63bb92862b9e33e5380f5222edcac013477f25d5971b0689d48df97606ad1d6befa3ea2965012ce2cb95f59717131f7c0a90b8521339902c51746e2a3eb821ccc6599af015578b46de2b25ee5e8799d203a9ebcc88b5d1c1c000731a06e5e238093939bfbbdb1140b24e2f8167c4b450579d19c6973131cbc21532aceffc2ed9b0a290e7414ec369f3bbe1b2566b8ad40cb4bbc492a3d555f94f15f38746c3a1212849a97bc06ecc26bd49e138ae19c8c324d3fa4870fe6396b7812e3d0af1f926edc7d6c9c49fb1d56a5a66623ccc972db0658164e4267bc529705f8d96642f229fc09e1e3330f9e550237a632a6be3790511da0676e5eb21f721fc5ac7f5a28b5b51e78fbc6635a953c8359037a151e1491b63176a28144ad00eb752366ac88dc64f2f0d3047cf49af1167a84e97410fa53eb544123e84efc6dee26bd7f8dd8698665164611a1a5886608575b9680c6636fdad66df86bc3f511b6cae1cec2ca6d87226328c5af9c328a15d2aea343c82c17bb3987a0dfff144e24749385f6825f86943fbb2c87ae24348372af2b1c143dac739bce12bd048a2bd134c473e2669f19043740d59d2a9d81d162c7c1470646d4794ab1f49f33e6b99efadceae479079ddc0d73cb5bb9ded9c9d3acf53adfc7fc28b86ffa4e8b69b7f7976ab8bd36dd95b78b95e11ed5082bef49a4ba41fa772fa08ed62ee9e0f8102a34b28579cb2ee79b3685c72975879f95bc193c5b3742718e76689a6899ca1d700399d9cc9b50ba7c1a9289460fb95ddc9afe2668003f4aa659c38ce46e14e15212d60b512a0bd78e75b1762abd9f471eb5e2f8370807f4b38900530b1c0aaf049f930c7b5db1b9160585434260f8bf1ec170a30b92c10eb6e831016d6a1c42f3fb9a11119ec41eeb6f1caabf0a877855dd401b08d57f2360a09d3da7a49c816c1ceeaf9a1d0befa7a9530219d6167f0d9077c129b1f150c850126abf8c1b01bab40721b733e93b34ee0cad41e6e4d2df21408690b60c1ec48f01bcb22a13300d3c35c47097bb54eb4623eba34eb7f077d104b8169674a07996802818f89cf101cbac3e7fcb0e09b1e310bf6877db29fa5a87d9470161a2ba492c894ca1a67c58062f4ad4e915b68e7341f028d4c18ba52e29c29dc32ac84ec78359067c5f9c75234c9d218119214a90322ebd055048582615336c9de230838c3a6e67a97c07552126c4a53116c8acf916556bcd38e4d1a840c6cb9c8e26f82ce32dc420cc06801cc6755d822e90fa7d85263abb058951e4740b9a8ce341daee2360c65390621f225e41218ad84a00d996a314f6ee2701e99e5e1007d10c01277581809c307a144f1f893e5f06e5c6223530eec821857f0cae6fedec87794d2842670b0f6745fbfb3052b0db6f066ef9a7403a1ac2e31bdaa110a1f28ae33894faa5999609d177a287041bc057da628f9caae22cc360804198e7f7b3179f945e8cc53d0a1553b546d6468863183794915887a4ff0b33906e7928d5594aad43639c2eb7bbe5e3ba63d70a4ccec197a4d8dee9b3cb2caa6ee6898af68f71fcb27a9c486774b8c3ca1643791b3d40118f09dff0e48db725dda99dfec3b20decb7d06853caaee07f2b4d3b8089dfcf344ed4b4fb951a939044ec337ae098080e83314f9ff715cc9f6eb2dfb82393010d34e970719abe2bbcdf2bab26b1c223cf1632ad9ac45b72ffc7492ef9285a43d6abac1ef0378a62eeb0702578e3780d34c37108e4fc38fc393ffda5e8def24449ea97c19952c3a2e0a7a9361459ed81ab2ceb0eef8998b84064d2cd6ccbba9261102df2fb13e5acbdaab0913080e0451ca1b747e905838507728a739431896e83aa7b8859a019bb903f520d76fad13885864f578a3ade05c66e8127be7e3cc7258f6596cd20e8dd64eb9801fc80e8a296b0cb58a964ed3fa83bde918f4f27aa8b88dce5de0fa5c5eae5d7ed6ff9428a505a9de6ec3340834b1cb2b0a46f5448ca97113e6facb5e66b522701f7f15b07bb5b402b1a04086cf836751e6d621b56e4b0080e43389fa3e3a99d10f29317b2e9e353bcc3a9e934aeafa1fd3ae34c56ee707993df1c0f1850ce26f45e7917079033ea9d17300816b9790c611c058439c73cf533a40d560a64df4717bc65bb2cbfe00f5b98fe24e86b37a80930500375ccd43f614bc9770584a611ad2fc9dbd16aa16559467ccbe88379eca5c47d967a77d34d35c3c8f44004bc001672f4a4fa5287eb06aaed11b0ff24c4e4686252f9a4943ef627a91c3323b2d53720ad1bde8b24fced9873c78d123d7dd95cc7b192ac867f0e07d1f848bc7834e7e8f35c177eefc069e6565bab71ee1473eae97ec5c23d653c08415e0d13937ad9e1485ee59242bf0ad9ab4c880eba15ff6496c49701b926f9dbb29f4c4fa465ee7d51c5122c9d33e39ec5e1eb0225095ea4550730e01a906a01f9afb2627b7533167898f4b217d848fd9845bdf3f3ffd80c12e5f7d9803ea8947a82f9887aae16a498f227240a6e534a60f9affbf5a91c3ef2ad77eb893840eedd5378b094807d61098e83add30584e0bd84a3db45448938747cb0c7337e12ce9e2b60ff2d3949c0d5fd22c5dd2caf14e8b47308b91e689617fa9e8b36aa25e340ed968def3303c17eace72a62face65d71f5121c073d6d8eb378fadf1d26345f87fafcd84bd7ada852564d5e8c60c4c48125492a0848c48ea00e8deea1d05233dde4c0d2e1850a1fda8f741973c5e4d2401ec0474b648f4f9b1ef294383d6451c263fcd1f2cc260e1dfe6bf22772bfee0a2ed070bdb60893ba2418a8251ae75d46aa43b859ea6c17316c058061075597c96780c3cac268ebfbc67f99b2b9883a42f9fa10c411f37c5aee2921bf2b4e531e9c14245269d172097bf962e402e2b7df6a68eeee8336213fbef825d8fc75e43eb9924d4fdd4cc349651143d291f0e964b58e04bca4866a0dee109a2849762f78c5918ab57a0698889461ed1776c853c3fe7aafcfe841284496ef9c67c7fdf8775fc393448a607b5ad76d0d7f324135293188a4ce4e6ee821888423282c0d9a72c04e92ae56a0188c1a5e2de95c7b67f88bd6c98f2c9d6402aa4421c9d8ce8f98ee68558bd4ab5c2afc7e57fa04abcdc6a4d1010ad9a0bfdc6f20b6c70fe1d1809571f1b4705a0fe239dcdb8a485dd9606145f228a2bcd201bf632a39a0e1b283be4f5e70ee483f159dca1fba75b743b0f17308837312db17eafc3da86e47a651a7175845378d8602806d630a62b277a2255d431f9f8d1c4271f9ae619a24a878150b00d2b2480d03dff5c432b0952fcdb782c52f5b30a584270f4abe378a91118d82b028989fc43380b55b9625931ae16495a302e0c758bc2476785caa13e63e21532f9900f1a227a03d47345d91a61fdd7f0832b8bf7d37519cdfb540742b1af32aa9d6501987e4b84c0454fe317ae19a53f84b1de060b046c61fd3855b0a4fe879a322fba5827aa75f1a2cfb1bda55929bcea356cccc5d73b2d88b6a4a6e08d3280e05015a9dccadc7cbd0684538750196e93a3d89504e77f4f2186acb615b78f3b0f446f1a65caa364b75ef7d0ca2c97c73f3bf8905089c50c95f39a34d58171af2bbf42d1802f40ee0970ac98a2a64097128779d5c925b32ddddfac2f2878ac230a3f0d2ff3ae09821bf293116a9446ffd107ecc27899f4254ffbcbb7ffc999bae0d8d0d02fe664a3ac9a07e20a5327e746cdd13f490aea652518a9d31d97038f146b8715e4e2f05e7d1b35eb2cb36d8f28ab700177c68e7dea57280e56f91ee1d5ccc57eee7ea5ffc743e070654d4d0cb3749d21d7cb6a277b05c5edad4dafe258351d78a26c2a614e923530d945ac6ac5ff06ef842ade6f8cb7eb07fa8686c85b4a5a5563f596046b8feb40d8ee5d76808061dabd63bf92152f24516e692e48a9131241ddf31ed2946699a32615cb422de1fb2e876b76a5690d27addefaec43d525fd3b77eb2cb4f2a793fe887d7d5df06f3423bc3c2ecfae4a52623c4f93b04f2f76fba74c54f5a4c6718d3711ea237b7267c0ee9d21be7947cb204eed323e178baa5ef28b4fbe61fb3bea5d6ac1043c6afd3925dd526e3ec142c2e449b2dee398b2cd55fa06e1612f6c078da134cea986462573e0c701695a0abfaeaa4f385525ca26e32ac26c2ee1c80010bf6a9ced7aeca8a33556eb1e9c17412c03913c1303c0f25fd829fc9c309abdd9aa0e410defae47dde29309c3d5dc3c912c833ff30e5904cb397fb6bf5e47ab8a652139708bd78019810c194e906bf2f205fd07acd6e7d6fd2288b72c78883410b5ad146c8adf0a7383fb8f7e775c847770fc23a4d90fbe1ac09aa97da111847fd1781f4a9ed80e6182bf329cb86e2d6d2941e892e6a9b2a5b25af285b50c410f6043a01de4efb2b2acd43f71882a2ab6c65312d143af78e58faf2b53bcd6b3cbd19bc77d18ff9c2fd8f0a2fe28ecba8c59f13d83bce7904949a5d0ed269b2ceb715f8add34fa2f72ec0af63e9206d7c1eca6dad33713f23f6598117fc54068cc7b93dcbd3dbac23d24dd43abbe5180efaa162e356b33b0ea99fbe231b5e4b46d1580940b3b85d6ded6d220bacbdb80afdd98b538996b5aee7ca0616a9866f349698eedb0d48a19a516e12a74f3fa500ba2bc9198a9034580fc92138030e486f8ddd84",
        }},
    ],
    "solution": str(random.randint(700, 868))
}

r = session.post("https://41bcdd4fb3cb.610cd090.us-east-1.token.awswaf.com/41bcdd4fb3cb/0d21de737ccb/cd77baa6c832/verify", headers=headers, json=payload)
if r.json()['inputs'] != "null":
    token = r.json()['token']
    print(f"\nToken: {token}")
else:
    print("\nFailed to get token...")

payload = {
    "awswaf_session_storage": None,
    "checksum": "7E116771",
    "client": "Browser",
    "existing_token": token,
    "metrics": [
        {"name": "12", "value": __number__(0.2), "unit": "2"},
        {"name": "200", "value": 1, "unit": "2"},
        {"name": "201", "value": 2, "unit": "2"},
        {"name": "13", "value": __number__(5.8), "unit": "2"},
        {"name": "10", "value": 0, "unit": "4"},
        {"name": "9", "value": 0, "unit": "4"},
        {"name": "11", "value": __number__(19.7), "unit": "2"},
    ],
    "signals": [
        {"name": "KramerAndRio", "value": {
            "Present": "zWctqBru/CzYe+H4::772711810aee175f7af5bdf529971cb8::727b462641f230bf77be7db6b4723cac3ab61a066c5a8451840830f67c90d30fbe84cc9ce71acc8f4d944f65f72fb172d681baae3e388aae1db13caecc6ef8521432d1a8c6ebe33d4991e05d254f2849ac3c3968aa57507a58d5a956f47e8bb2e649ae050d94a4bfe22a0821f7f66c6022948f7a2345371f09b6fc48430899d3dbd0ae9e205d1255d0abf632e77cc17935f7245104d5a7eb7410911769a87d6df9a00deff73bce23ff009653059f4048f3ba468c4053365c8a76fcad5ef9fb60247854eb7bf4905af9e15a5340dabdffeca9ca4f84a12eb8f33231ca965212551c8c3a554346baf12720569704ba13e6561f8d92d8",
        }},
    ]
}

r = session.post("https://41bcdd4fb3cb.610cd090.us-east-1.token.awswaf.com/41bcdd4fb3cb/0d21de737ccb/cd77baa6c832/telemetry", headers=headers, json=payload)
if "token" in r.json():
    token = r.json()['token']
    interval = r.json()['next_interval']
    awswaf_session_storage = r.json()['awswaf_session_storage']
    print(f"\n{token}")
    print(awswaf_session_storage)
    print(f"Interval: {interval}")
else:
    print("\nFailed to get token / session_storage...")

r = session.get("https://41bcdd4fb3cb.610cd090.us-east-1.captcha.awswaf.com/41bcdd4fb3cb/0d21de737ccb/cd77baa6c832/problem?kind=visual&domain=efw47fpad9.execute-api.us-east-1.amazonaws.com&locale=es")
if "validity_duration" in r.json() and r.json()["validity_duration"] == 60:
    problem_type = r.json()['problem_type']
    if problem_type == "toycarcity":
        print("Toycarcity...")
        exit()
    else:
        iv = r.json()['state']['iv']
        payload = r.json()['state']['payload']
        key = r.json()['key']
        hmac_tag = r.json()['hmac_tag']
        images = json.loads(r.json()['assets']['images'])
        target = r.json()['assets']['target'].replace('["', '').replace('"]', '').capitalize()
        target0 = r.json()['localized_assets']['target0'].capitalize()
        validity = r.json()['validity_duration']

    print("\nProblem_type:", problem_type)
    print("Iv:", iv)
    print("Payload:", payload)
    print("Key:", key)
    print("Hmac_tag:", hmac_tag)
    print("Target:", target)
    print("Target0:", target0)
    print("Validity:", validity)
    Logger.captcha(f"Question,Select all images that contains {target},Select")
else:
    print("\nFailed to get image challenge...")

total = 1

def __saveImage__(image):
    data = base64.b64decode(image)
    file = os.path.join('temp', f"{uuid.uuid4().hex[:32]}.png")

    with open(file, 'wb') as f:
        f.write(data)
    
    answers = []
    images = []

    model = tf.keras.models.load_model('model.keras')
    test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

    test_generator = test_datagen.flow_from_directory(
        'dataset',
        target_size=(100, 100),
        batch_size=1,
        class_mode='categorical',
        shuffle=False
    )

    img = load_img(file, target_size=(100, 100))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions[0])

    class_indices = test_generator.class_indices
    predicted_class = [k for k, v in class_indices.items() if v == predicted_class_index][0]

    images.append(f"{file} -> {predicted_class}")
    if predicted_class == target:
        answers.append(file)

    for image in images:
        print(f"Predicted Image: {image}")

    for answer in answers:
        print(f"Image -> {file} | True {total}")
    
    os.remove(file)

for idx, image in enumerate(images):
    __saveImage__(image)
