import redis
from flask import abort

from src.rely.utils.configs import AppConfig


class CacheManager:
    def __init__(self, page_number: int,ac: AppConfig):
        self.ac = ac
        self.page = page_number
    def __repr__(self):
        return f"CacheManager(page_number={self.page}, ac={self.ac})"

    def get_properties_for_given_address(self, address: str):
        try:
            return self.ac.redis.get(address)
        except Exception as e:
            abort(500, f"err-while-retreiving-from-cache => ${e}")

    def get_nearby_properties_from_zip(self, zip: str, start_index: int, end_index: int):
        try:

            return self.ac.redis.lrange(zip,0,-1)
        except Exception as e:
            abort(500, f"err-while-retrieving-files-from-zip-code => ${e}")

    def get_properties_by_city(self, city):
        try:
            pass
        except Exception as e:
            abort(500, f"err-while-retreiving-properties-by-city {e}")


    def get_suggestions_for_key_strokes(self, address: str):
        max_suggestions = 8
        results = []
        range = 50
        start_index = self.ac.redis.zrank('autocomplete', address)
        if not start_index:
            return []
        while (len(results) != max_suggestions):
            matched_indexes = self.ac.redis.zrange('autocomplete', start_index, start_index + range - 1)
            start_index += range
            if not matched_indexes or len(matched_indexes) == 0:
                break
            each_address = [addr.decode() for addr in matched_indexes]
            for address in each_address:
                minlen = min(len(address), len(address))
                if address[0:minlen] != address[0:minlen]:
                    max_suggestions = len(results)
                    break
                if address[-1] == "%" and len(results) != max_suggestions:
                    results.append(address[0:-1])

        return results

