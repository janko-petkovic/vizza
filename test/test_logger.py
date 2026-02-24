from vizza import SimpleLogger as sl

sl.info("Information")
sl.warning("Warning")
sl.error("Error")
sl.success("Success")

sl.info("Information", "Multiline")
sl.warning("Warning", "Multiline")
sl.error("Error", "Multiline")
sl.success("Success", "Multiline")
