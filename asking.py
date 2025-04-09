#User Information Program

def get_user_info():
    """Get user information"""
    
    # Ask for user's name
    name = input("Please enter your name: ")
    
    # Ask for user's gender
    gender = input("Please enter your gender (Male/Female/Other): ")
    
    # Ask for user's location
    location = input("Please enter your location (City/Country): ")
    
    # Ask for user's nationality
    nationality = input("Please enter your nationality: ")
    
    # Return user information
    return name, gender, location, nationality

def print_user_info(name, gender, location, nationality):
    """Print user information"""
    
    # Print user information
    print("\nUser Information:")
    print("--------------------")
    print(f"Name: {name}")
    print(f"Gender: {gender}")
    print(f"Location: {location}")
    print(f"Nationality: {nationality}")

def main():
    """Main function"""
    
    # Get user information
    name, gender, location, nationality = get_user_info()
    
    # Print user information
    print_user_info(name, gender, location, nationality)

if __name__ == "__main__":
    main()
