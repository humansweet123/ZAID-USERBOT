from os import getenv

API_ID = int(getenv("API_ID", "26143166")) #optional
API_HASH = getenv("API_HASH", "6d272cb777a34f9050396cc60993e15c") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5480218118").split()))
OWNER_ID = int(getenv("OWNER_ID", "5480218118b"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://humansweet:<password>@cluster0.vuehb51.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5841954743:AAFkYLhHD_5VEmjQpK4ds3w5WTO_rodGAd8")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")

STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAjnaUPgEruZjQAmHGDY5Y_S5akIrSXcqn7BG0Al0Ko96cTZn8MwiS_kmJdimjfqh8gOvXZtJIiB7W7N_R-kPaXa0akUS6Vi-CtYOe2FfEyEgzuPbLnrGSVossIy5xzVEW1VKdSu8bhrfKPfKoEwJYqNim74bbIrh4IGPlhRd4nh6VIPjhOJvy1Gnl_ozgGtcxajfl1FT1j_9aerOyq9oLZN-SlJoQ3hfqqlGur10nFqXNhg6HRuEkLsRSpOphn4zAIlM2XrvZm4Wr--bfPupuIqhsClhCBFW-LxxSQaQRblWslVamfW16C65lDqbmM508eoyGwJj1NMw9wfoKvHlvEAAAAAFGpX4GAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
