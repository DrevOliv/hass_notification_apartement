import requests
import re
import json


class API:
    def __init__(self):
        self.headers = {
            'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            # 'Cookie': 'Fast2User_language=sv; PLAY_SESSION=eyJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7InV1aWQiOiJkYzViYTI3Yy1mYzU4LTQ1YzMtODk5NC02ZmRiM2RlNjc1YjIifSwibmJmIjoxNzIzNjU4OTQ1LCJpYXQiOjE3MjM2NTg5NDV9.3qOArWUOvu2nADd8O8M3twWn-RcfipiT_eM1vDDmxqc; _gcl_au=1.1.591211750.1723658947; _gid=GA1.2.1836436409.1723658947; _gac_UA-7225551-1=1.1723658947.Cj0KCQjwq_G1BhCSARIsACc7NxrdbED87ZecEhlVlWQ9dAICq_Pj8s_UPZj3A05CxIkmfq-ziXaRrCwaAtZ3EALw_wcB; _hjSession_3110052=eyJpZCI6ImI2N2ZmOTg5LTIyOTgtNGMzMy1hY2M2LTNhZjc4OGQzMTY4MiIsImMiOjE3MjM2NTg5NDc1NjIsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _hjSessionUser_3110052=eyJpZCI6ImI2ZjY4YTJkLTlhMDMtNTQ0Mi1iYWI5LWRjMjdlOTE0ZjQ5YyIsImNyZWF0ZWQiOjE3MjM2NTg5NDc1NjEsImV4aXN0aW5nIjp0cnVlfQ==; _gcl_aw=GCL.1723659027.Cj0KCQjwq_G1BhCSARIsACc7NxrdbED87ZecEhlVlWQ9dAICq_Pj8s_UPZj3A05CxIkmfq-ziXaRrCwaAtZ3EALw_wcB; _gcl_gs=2.1.k1$i1723659026; _hjDonePolls=893912%2C892780%2C893910; _gat_UA-7225551-1=1; _ga_NRCTZXRQJV=GS1.1.1723658947.1.1.1723659549.0.0.0; _ga=GA1.1.1235792807.1723658947',
            'Origin': 'https://www.studentbostader.se',
            'Referer': 'https://www.studentbostader.se/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
        }

        self.params = {
            'actionId': '',
            'omraden': '',
            'egenskaper': '',
            'oboTyper': 'SA1',
            'callback': 'jQuery37109752710397354891_1723659549380',
            'widgets[]': [
                'objektfilter@lagenheter',
                'objektsortering',
                'paginering@lagenheter',
                'objektlistabilder@lagenheter',
                'pagineringgonew@lagenheter',
                'pagineringlista@lagenheter',
                'pagineringgoold@lagenheter',
            ],
            '_': '1723659549381',
        }

    def get_list_of_apartments(self):
        response = requests.get('https://marknad.studentbostader.se/widgets/', params=self.params, headers=self.headers, verify=False)

        json_str = re.sub(r'^jQuery\d+_\d+\(|\);$', '', response.text)

        return json.loads(json_str)["data"]["objektlistabilder@lagenheter"]