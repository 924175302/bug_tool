import json
import requests


def bug_tool():
    url = "https://rct-ai.atlassian.net/gateway/api/xpsearch-aggregator/quicksearch/v1"
    header = {
        "content-type":"application/json"
    }
    cookie = {"ajs_anonymous_id":"%22772a5426-d38d-40f4-91c7-ceedc0d30a3f%22","atlassian.xsrf.token":"725e5e66-f148-4f2e-a701-9a168378c0b7_915a752f7e92125592119d503a6421be0f538441_lin","jira.navigation.expandableMenuStates.classic-issues-setttings":"{%22submenuActive%22:false%2C%22expanded%22:true}","jira.navigation.expandableMenuStates.classic-apps-setttings":"{%22submenuActive%22:false%2C%22expanded%22:true}","JSESSIONID":"1FEE672FBE81D9B263B80015D9998C0","cloud.session.token":"eyJraWQiOiJzZXNzaW9uLXNlcnZpY2VcL3Byb2QtMTU5Mjg1ODM5NCIsImFsZyI6IlJTMjU2In0.eyJhc3NvY2lhdGlvbnMiOltdLCJzdWIiOiI2Mjk3MDdlYjU2M2QzODAwNjhiMWQ3NzMiLCJlbWFpbERvbWFpbiI6InJjdC5haSIsImltcGVyc29uYXRpb24iOltdLCJjcmVhdGVkIjoxNjU0MDY1NDU4LCJyZWZyZXNoVGltZW91dCI6MTY1NjM4ODI3NywidmVyaWZpZWQiOnRydWUsImlzcyI6InNlc3Npb24tc2VydmljZSIsInNlc3Npb25JZCI6IjhlZTU3N2VjLWM1N2ItNGU0Yy1hZDc4LTYwZjM4YTYxY2MzZSIsInN0ZXBVcHMiOltdLCJhdWQiOiJhdGxhc3NpYW4iLCJuYmYiOjE2NTYzODc2NzcsImV4cCI6MTY1ODk3OTY3NywiaWF0IjoxNjU2Mzg3Njc3LCJlbWFpbCI6IndhbmdsaWppZUByY3QuYWkiLCJqdGkiOiI4ZWU1NzdlYy1jNTdiLTRlNGMtYWQ3OC02MGYzOGE2MWNjM2UifQ.Vkm7Ea_muGHtWfFfTh-Oxq6oxTQeR6PANjb4VbWUW2a3-2mGmUl3NOlmAO6l7i_dQKM5slYvY4n1c8zFE8MPPkR5XqXjMGgyGMmKd8HVIa90hPMpXaUeUdlI-wUqc5rLYYA-UXLgP9ORFHNzLUBW6B5lMb4df0Y3VuGcgWkkiFv-QilDFI6zuOMV6TGVZobfbILJdyqJoWQyLvH2B5sji4-ddz3g71Y5hUKU_FN-mULEo5Wq5yrTdS70VaFOvzxQ1f8vy_SWGVhgtKSj3-51aA4AG8BvBpgU1IyGm8u8_ioToBIKjGPdtnPP9VQhn4EmNEnpDqbVHDHOHK47BcU2rw"}

    query = {"query":"","cloudId":"54cc4c96-c35c-40fa-8ed3-81f8781efc95","limit":50,"scopes":["jira.issue"],"filters":[],"searchSession":{"sessionId":"544f07d7-e066-4d6e-b6d0-25967503f3f2","referrerId":None},"experience":"jira.nav-v3","cloudIds":[]}

    resp = requests.post(url, data=json.dumps(query), headers=header,  cookies=cookie)
    #print(resp.json()['scopes'][0]['results'])



if __name__ == '__main__':
    bug_tool()