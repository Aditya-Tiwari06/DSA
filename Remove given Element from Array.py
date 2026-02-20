def remove_element(arr, element):

    try:
        arr.remove(element)  # Removes first matching element
        print(f"Element {element} removed successfully.")
    except ValueError:
        print(f"Element {element} not found in the array.")
    return arr


def main():
    try:
        # Input array from user
        size = int(input("Enter number of elements in array: "))
        if size < 0:
            print("Size cannot be negative.")
            return
        
        arr = []
        for i in range(size):
            val = input(f"Enter element {i+1}: ")
            arr.append(val)  # Storing as string; can be converted if needed

        print("Original Array:", arr)

        # Element to remove
        element = input("Enter element to remove: ")

        # Remove element
        updated_arr = remove_element(arr, element)

        print("Updated Array:", updated_arr)

    except ValueError:
        print("Invalid input. Please enter valid numbers where required.")


if __name__ == "__main__":
    main()