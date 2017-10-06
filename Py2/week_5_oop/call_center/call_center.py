class Call(object):
    def __init__(self, call_id, name, phone_number, time, reason):
        self.id = call_id
        self.name = name
        self.phone_number = phone_number
        self.time = time
        self.reason = reason

    def display(self):
        info = {
            "Call ID: ": self.id,
            "Name: ": self.name,
            "Phone Number: ": self.phone_number,
            "Call Time: ": self.time,
            "Reason for Call: ": self.reason
        }
        return info

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.size = 0

    def addCall(self, id, name, phone_number, time, reason):
        call = Call(id, name, phone_number, time, reason)
        self.calls.append(call)
        return self.calls

    # def displayCalls(self):
    #     for call in self.calls:
    #         info = call.display()
    #         for attribute in info:
    #             print attribute + str(info[attribute])
    #         print "-" * 20

    def remove(self):
        self.calls.pop(0)

    def info(self):
        for call in self.calls:
            info = call.display()
            call_attr = info.keys()
            call_info = info.values()
            print call_attr[4], call_info[4]
            print call_attr[2], call_info[2]
            

            print "-" * 20
           
        count = 0

        for call in self.calls:
            count +=1
        print "There are {} calls in the queue".format(count)







center = CallCenter()
center.addCall(1, "Jane", "773-555-1212", "20:30", "Tech Support")
center.addCall(2, "Bob", "312-555-1212", "20:40", "Repairs")
center.addCall(3, "Gertrude", "847-555-1212", "20:50", "Customer Service")
# center.remove()
center.info()


# queue = [call1, call2, call3]

# for call in queue:
#     info = call.display()
#     for attribute in info:
#         print attribute + str(info[attribute])
#     print "-" * 20