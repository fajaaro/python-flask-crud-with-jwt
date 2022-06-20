class MainHelper:
    @staticmethod
    def serialize_objects(objects):
        return [obj.to_json() for obj in objects]