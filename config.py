import enum

API_TOKEN = ""
db_file = "database.vdb"


class States(enum.Enum):
    S_START = "0"
    S_READY = "1"
    S_CONSENT = "2"
    S_GROUP = "3"
    S_MARKS1 = "4"
    S_ESTIMATE_211_1 = "9"
    S_ESTIMATE_212_1 = "10"
    S_ESTIMATE_213_1 = "11"
    S_ESTIMATE_GRADE_211_1 = "15"
    S_ESTIMATE_GRADE_212_1 = "16"
    S_ESTIMATE_GRADE_213_1 = "17"
    S_ESTIMATE_211_2 = "12"
    S_ESTIMATE_212_2 = "13"
    S_ESTIMATE_213_2 = "14"
    S_ESTIMATE_GRADE_211_2 = "18"
    S_ESTIMATE_GRADE_212_2 = "19"
    S_ESTIMATE_GRADE_213_2 = "20"
    S_ESTIMATE_RESULT1 = "5"
    S_MARKS2 = "6"
    S_ESTIMATE_RESULT2 = "7"
    S_END = "8"
