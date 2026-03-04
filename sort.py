from openevolve import run_evolution, evolve_function, Config
import yaml 

config = Config.from_yaml("ollama_config.yaml")

# Evolution with inline code (no files needed!)
# result = run_evolution(
#     initial_program='''
#     def fibonacci(n):
#         if n <= 1: return n
#         return fibonacci(n-1) + fibonacci(n-2)
#     ''',
#     evaluator=lambda path: {"score": benchmark_fib(path)},
#     iterations=100
# )

# Evolve Python functions directly
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr

result = evolve_function(
    bubble_sort,
    test_cases=[([3,1,2], [1,2,3]), ([5,2,8], [2,5,8])],
    iterations=50,
    config=config
)

print(f"Evolved sorting algorithm: {result.best_code}")