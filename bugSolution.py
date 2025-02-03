def function_with_improved_error_handling(data):
    if not isinstance(data, list):
        print("Error: Input data must be a list.")
        return []

    result = []
    for item in data:
        if item is None:
            continue
        elif isinstance(item, dict) and 'value' in item:
            try:
                result.append(item['value'])
            except (KeyError, TypeError) as e:
                print(f"Error processing dictionary item: {e}")
        else:
            print(f"Warning: Skipping invalid item: {item}")

    return result

data = [{'value': 1}, {'other': 2}, {'value': 3, 'extra': 4}, None, 123, {'value':'a'}]
result = function_with_improved_error_handling(data)
print(result) # Output: [1, 3, 'a']

data = []
result = function_with_improved_error_handling(data)
print(result) # Output: []

data = 123
result = function_with_improved_error_handling(data)
print(result) # Output: Error: Input data must be a list.
[] 