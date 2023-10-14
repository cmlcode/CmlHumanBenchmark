from webdriver import DriverFactory
from benchmarks import Benchmarks

def main():
    driver_factory = DriverFactory()
    driver_factory.add_maximized()
    driver_factory.add_detached()
    driver = driver_factory.create_driver() 
    benchmarks = Benchmarks(driver = driver)
    reaction_time = benchmarks.play_reaction_time()
    print(f"Reaction time: {reaction_time}")
    driver.close()
    

if __name__ == "__main__":
    main()