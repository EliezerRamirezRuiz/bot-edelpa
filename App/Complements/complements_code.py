import requests

base_url = 'https://discordapp.com/api/webhooks/'

complement={'General':'1088085873469423638/h89WN8y-vvQTTQhwu6Fszm6HuLhZ4QaVICxMyAfdudrizbV4QBCknwTYgv7H3U2VSGPa',
            '1':'1088153137719812147/_DTsIubqBG3Mvk-t4uRTPYDDuPdAsxIIIXSVbuFb4t4VB4xKm0NoCjLVUHOiNBxsggDb',
            'a':'1088149916154609694/zHNOIGFlyfucsD_zfb4j7G3UDxJ_U8oNTnG3T-OPRnGDZX3vrzpPMTLkouQJ-Jc_Fv87',
            'vds':'1088161911612391585/zFz87AW8vIC9nXry7jZP8ZfG59aUERv9HY-bN6VIlYGPMQ77vj2ZBiELXZt_iXwmZd95',
            'canal de patricio':'1088163688369893527/znqHKr6D1qpbNXxzwIwqw0xKE_0ov-r-UzMAMQVvasgV_G4lfpnTuwBs9L6tmx5B6VRL'
            }


for i, (key, value) in enumerate(complement.items()):
    webhook_url = f'{base_url+value}'
    message_content = 'Hello, Patricio!'
    response = requests.post(webhook_url, json={'content': message_content,})