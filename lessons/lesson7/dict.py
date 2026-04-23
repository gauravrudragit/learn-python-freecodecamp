# Dictionaries

band = {
    "vocal": "Plant",
    "guitar": "Page"
}

band2 = dict(vocal='Plant', guitar='Page')

print(band)
print(band2)

print(type(band))
print(len(band))

print(band["vocal"])
print(band.get("guitar"))

print(band.keys())
print(band.values())

print(band.items())

print("guitar" in band)
print("page" in band)

band["vocal"] = "newVocal"
band.update({"bass": "JPJ"})
print(band)

print(band.pop("bass"))
print(band)

print(band.popitem())
print(band)

band2["drum"] = "ned"
print(band2)
del band2["drum"]
print(band2)
band2.clear()
print(band2)

del band2

# Copy dict

# band2 = band
# band["a"] = "b"
# print(band2)

band2 = band.copy()
band2["vocal"] = "b"
band2["new"] = "new"
print(band)
print(band2)

band3 = dict(band)
print(band3)


# Nested dict

mem1 = {"name": "plant", "inst": "vocal"}
mem2 = {"name": "page", "inst": "guitar"}
band = {
    "mem1": mem1,
    "mem2": mem2
}

print(band)
print(band["mem1"]["name"])

# Sets

nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4, 5))

print(nums)
print(nums2)

# nums = {1, True, 2, False, 2, 3, 0}
# print(nums)

# nums = {1, True, 5, 4, 3, 0, False}
# print(nums)

print(nums.union(nums2))
# nums.intersection_update(nums2)
# print(nums)
print(nums.symmetric_difference_update(nums2))
print(nums)
