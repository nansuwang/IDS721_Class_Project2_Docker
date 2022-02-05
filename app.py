import uvicorn
from fastapi import FastAPI
import random
from klargest import klargest

app = FastAPI()


@app.get("/")
def read_main():
    return {"msg": "Hello World!"}


@app.get("/{name}")
def get_name(name: str):
    return {"Welcome To the API": f"{name}"}


@app.post("/predict")
def find_klargest(data: klargest):
    data = data.dict()
    nums = data["nums"]
    k = data["k"]

    if not nums:
        return None
    n = len(nums)
    if k > n:
        return None

    def partition(left, right, pivot):
        if left < 0 or right >= n or left > right:
            return

        target = nums[pivot]
        ind = left
        nums[pivot], nums[right] = nums[right], nums[pivot]

        for i in range(left, right):
            if nums[i] > target:
                nums[i], nums[ind] = nums[ind], nums[i]
                ind += 1

        nums[ind], nums[right] = nums[right], nums[ind]
        return ind

    def quickselection(left, right):
        if left < 0 or right >= n or left > right:
            return

        pivot = random.randint(left, right)
        pivot = partition(left, right, pivot)
        if pivot == k - 1:
            return
        elif pivot > k - 1:
            quickselection(left, pivot - 1)
        else:
            quickselection(pivot + 1, right)

    quickselection(0, n - 1)

    return {"The k-largest number is ": nums[k - 1]}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
