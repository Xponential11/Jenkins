from testBabyName import testBabyName

if __name__ == "__main__":
    test = testBabyName("baby1992.html", "baby1992.html.summary")
    test.setup()
    test.run()
    test.checkoutput("baby1992.html.output")
    test.teardown()