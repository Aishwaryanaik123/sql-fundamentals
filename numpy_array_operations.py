import numpy as np
import time


# 1. CREATE 1D, 2D AND 3D NUMPY ARRAYS
# 1D Array
arr_1d = np.array([10, 20, 30, 40, 50])

print("1D Array:")
print(arr_1d)
print("Shape:", arr_1d.shape)


# 2D Array
arr_2d = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\n2D Array:")
print(arr_2d)
print("Shape:", arr_2d.shape)


# 3D Array
arr_3d = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print("\n3D Array:")
print(arr_3d)
print("Shape:", arr_3d.shape)



# 2. MANIPULATE ARRAYS
print("\n--- Array Manipulation ---")

# Reshape
arr = np.arange(1, 13)
reshaped = arr.reshape(3, 4)

print("Original Array:")
print(arr)

print("\nReshaped Array:")
print(reshaped)

# Transpose
print("\nTranspose:")
print(reshaped.T)



# 3. VECTORIZED OPERATIONS
print("\n--- Vectorized Operations ---")

numbers = np.array([10, 20, 30, 40, 50])

# Addition
print("Addition:")
print(numbers + 5)

# Multiplication
print("Multiplication:")
print(numbers * 2)

# Subtraction
print("Subtraction:")
print(numbers - 5)

# Division
print("Division:")
print(numbers / 2)

# Square
print("Square:")
print(numbers ** 2)



# 4. AGGREGATE OPERATIONS ACROSS AXES
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\n--- Aggregate Operations ---")

print("Total:", np.sum(data))

# axis=0 → column-wise
print("Column Sum:")
print(np.sum(data, axis=0))

# axis=1 → row-wise
print("Row Sum:")
print(np.sum(data, axis=1))

print("Column Mean:")
print(np.mean(data, axis=0))

print("Row Mean:")
print(np.mean(data, axis=1))

print("Maximum:", np.max(data))
print("Minimum:", np.min(data))



# 5. BOOLEAN MASKING
print("\n--- Boolean Masking ---")

numbers = np.array([10, 25, 30, 45, 50, 65, 70])

# Select values greater than 40
mask = numbers > 40

print("Boolean Mask:")
print(mask)

print("Values greater than 40:")
print(numbers[mask])

# Direct boolean filtering
print("Values less than or equal to 40:")
print(numbers[numbers <= 40])



# 6. FANCY INDEXING
print("\n--- Fancy Indexing ---")

numbers = np.array([10, 20, 30, 40, 50, 60])

# Select positions 0, 2 and 4
selected = numbers[[0, 2, 4]]

print("Original Array:")
print(numbers)

print("Selected Values:")
print(selected)


# Fancy indexing in 2D array
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\nSelected rows:")
print(data[[0, 2]])

print("\nSelected individual elements:")
print(data[[0, 1, 2], [2, 1, 0]])



# 7. STATISTICAL MEASURES
print("\n--- Statistical Measures ---")

scores = np.array([45, 50, 55, 60, 65, 70, 75, 80, 85])

# Mean
print("Mean:", np.mean(scores))

# Standard deviation
print("Standard Deviation:", np.std(scores))

# Percentiles
print("25th Percentile:", np.percentile(scores, 25))
print("50th Percentile:", np.percentile(scores, 50))
print("75th Percentile:", np.percentile(scores, 75))

# Median
print("Median:", np.median(scores))



# 8. CORRELATION
print("\n--- Correlation ---")

study_hours = np.array([1, 2, 3, 4, 5, 6])
exam_scores = np.array([50, 55, 65, 70, 80, 90])

correlation_matrix = np.corrcoef(study_hours, exam_scores)

print("Correlation Matrix:")
print(correlation_matrix)

correlation = correlation_matrix[0, 1]

print("Correlation between study hours and exam scores:")
print(correlation)



# 9. NUMPY PERFORMANCE VS PYTHON LOOP
#    1 MILLION ROW DATASET
print("\n--- NumPy vs Python Loop Performance ---")

# Create 1 million values
data = np.arange(1_000_000)


# Python Loop
start_time = time.time()

loop_result = []

for value in data:
    loop_result.append(value * 2)

loop_time = time.time() - start_time



# NumPy Vectorized Operation

start_time = time.time()

numpy_result = data * 2

numpy_time = time.time() - start_time



# Display Results

print("First 10 loop results:")
print(loop_result[:10])

print("\nFirst 10 NumPy results:")
print(numpy_result[:10])

print("\nPython Loop Time:", loop_time, "seconds")
print("NumPy Time:", numpy_time, "seconds")

if numpy_time > 0:
    print("NumPy is approximately",
          round(loop_time / numpy_time, 2),
          "times faster than the Python loop.")