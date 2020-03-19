import dependency_functions,time

if __name__ == "__main__":
    try:
        print(dependency_functions.git_pull())
        print("-"*70 + "Done" + "-"*70)
    except Exception as e:
        print(e)
        time.sleep(10)
