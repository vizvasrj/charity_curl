
import csv
from curl import get_level1, get_level2, get_peoples

abn = []
with open('1000 ABN.csv') as csvfile:
    csv_reader = csv.reader(csvfile)
    for idx, row in enumerate(csv_reader):
        if idx == 0:
            # print(row)
            pass
        else:
            abn.append(row[0])

peoples_array = []

# for idx, x in enumerate(abn):
#     print(idx)
#     # if idx == 0:
#     result = None
#     try:
#         result = get_level1(x).get("results")[0].get("uuid")
#     except:
#         print(f"Error in get_level1 except {abn}")
#     if result != None:
#         try:
#         # print("Not none")
#             charaty_json = get_level2(result)
#             get_peoples(charaty_json, peoples_array)
#         except:
#             print(f"Error in get_level2  except {abn}")


def process_abn(abn):
    try:
        result = get_level1(abn).get("results")[0].get("uuid")
        if result:
            charaty_json = get_level2(result)
            get_peoples(charaty_json, peoples_array)
    except Exception as e:
        print(f"Error processing ABN {abn}: {str(e)}")

from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor() as executor:
    executor.map(process_abn, abn)


from collections import Counter

occurrences = Counter(peoples_array)

# Find the maximum occurrence count
max_count = max(occurrences.values())

# Find the elements with the maximum occurrence
max_elements = [element for element, count in occurrences.items() if count == max_count]

# Print the maximum occurrence and the corresponding elements
print(f"Maximum occurrence: {max_count}")
print(f"Elements with maximum occurrence: {max_elements}")