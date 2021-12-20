def from_hex(char):
    if char == '0':
        return '0000'
    elif char == '1':
        return '0001'
    elif char == '2':
        return '0010'
    elif char == '3':
        return '0011'
    elif char == '4':
        return '0100'
    elif char == '5':
        return '0101'
    elif char == '6':
        return '0110'
    elif char == '7':
        return '0111'
    elif char == '8':
        return '1000'
    elif char == '9':
        return '1001'
    elif char == 'A':
        return '1010'
    elif char == 'B':
        return '1011'
    elif char == 'C':
        return '1100'
    elif char == 'D':
        return '1101'
    elif char == 'E':
        return '1110'
    elif char == 'F':
        return '1111'
    else:
        raise Exception('input not hex')

def bin_3(string):
    if string == '000':
        return 0
    elif string == '001':
        return 1
    elif string == '010':
        return 2
    elif string == '011':
        return 3
    elif string == '100':
        return 4
    elif string == '101':
        return 5
    elif string == '110':
        return 6
    elif string == '111':
        return 7
    else:
        raise Exception('not a bin_3 param')

def bin_n(string):
    num = 0
    for i in range(len(string)):
        index = (i + 1) * -1
        if string[index] == '1':
            num += 2 ** i
    return num

# for encapsulating and processing the stream of hex and binary
class BITS:
    data = None # datastream
    window = None # current translated binary
    byte_pointer = None # where in the datastream we are
    bit_pointer = None # where in the window we are
    eof = False
    
    def __init__(self, hex_data):
        self.data = hex_data
        self.window = from_hex(self.data[0]) + from_hex(self.data[1])
        self.byte_pointer = 2 # pointing to next char in data to read
        self.bit_pointer = 0
        self.eof = False
    
    def get(self, num_bits):
        while num_bits + self.bit_pointer > len(self.window):
            self.extend()
        output = self.window[self.bit_pointer:(self.bit_pointer + num_bits)]
        self.bit_pointer += num_bits
        return output
    
    def extend(self):
        if not self.eof:
            self.window += from_hex(self.data[self.byte_pointer]) + from_hex(self.data[self.byte_pointer+1])
            self.byte_pointer += 2
            self.eof = self.byte_pointer >= len(self.data)
    
    def clean(self):
        if self.eof:
            self.window = ''
        else:
            self.window = from_hex(self.data[self.byte_pointer]) + from_hex(self.data[self.byte_pointer+1])
            self.byte_pointer += 2
            self.eof = self.byte_pointer >= len(self.data)

    def parse(self, max_len = None):
        version = bin_3(self.get(3))
        type_ID = bin_3(self.get(3))
        payload = ''
        if max_len != None:
            max_len -= 6
        if type_ID == 4: # literal value
            flag = '1'
            while flag == '1':
                flag = self.get(1)
                payload += self.get(4)
                if max_len != None:
                    max_len -= 5
            payload = bin_n(payload)
        else: # operator
            length_type_id = self.get(1)
            payloads = []
            if length_type_id == '0':
                # by num bits
                op_len = bin_n(self.get(15))
                if max_len != None:
                    max_len -= 16 + op_len
                    if max_len < 0:
                        raise Exception('nested operation out of bounds')
                while op_len > 0:
                    v_next, op_len, payload = self.parse(op_len)
                    version += v_next
                    payloads.append(payload)
            else:
                # by num packets
                num_packs = bin_n(self.get(11))
                if max_len != None:
                    max_len -= 12
                for i in range(num_packs):
                    v_next, max_len, payload = self.parse(max_len)
                    version += v_next
                    payloads.append(payload)
            if type_ID == 0: # sum
                payload = sum(payloads)
            elif type_ID == 1: # product
                payload = 1
                for num in payloads:
                    payload *= num
            elif type_ID == 2: # minimum
                payload = min(payloads)
            elif type_ID == 3: # maximum
                payload = max(payloads)
            elif type_ID == 5: # >
                if payloads[0] > payloads[1]:
                    payload = 1
                else:
                    payload = 0
            elif type_ID == 6: # <
                if payloads[0] < payloads[1]:
                    payload = 1
                else:
                    payload = 0
            elif type_ID == 7: # =
                if payloads[0] == payloads[1]:
                    payload = 1
                else:
                    payload = 0
            else:
                raise Exception('type_ID error')
        return version, max_len, payload


with open('input.txt') as file:
    to_parse = file.readline().strip()
    parser = BITS(to_parse)
    versions = 0
    operating = False
    by_bit = None
    op_len = None
    sub_packs = None
    while not parser.eof:
        v_next, toss, value = parser.parse()
        parser.clean()
        versions += v_next
        print(value)
    print(versions)
    