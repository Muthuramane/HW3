 = "UNRESOLVED"

def ddmin(filename):
    if not os.path.exists(filename):
        print "File name doesn't exist"
        return
    try:
        p = xmlproc.XMLProcessor()
        ret = p.parse_resource(filename)
    except UnboundLocalError as exc:
        print "Test: %s" % FAIL
    except:
        print "Test: %s" % UNRESOLVED
    else:
        print "Test: %s" % PASS



if __name__ == "__main__":
    print "Delta debugging\n"
    filename = str(sys.argv[1])
    print "Given Filename: %s" % filename
    print

    ddmin(filename)



