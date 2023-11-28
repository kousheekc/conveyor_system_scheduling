import random
import xlsxwriter

class OrderManager:
    def __init__(self, orders: dict) -> None:
        self.orders = orders
        self.schedule = []

    def generate_random_schedule(self) -> list:
        self.schedule = []
        for product, order in self.orders.items():
            self.schedule.extend([product] * order.total)
        random.shuffle(self.schedule)
    
    def set_schedule(self, schedule: list) -> None:
        self.schedule = schedule

    def get_schedule(self) -> list:
        return self.schedule
    
    def write2excel(self, name):
        workbook = xlsxwriter.Workbook(name)
        worksheet = workbook.add_worksheet()        												
        worksheet.write('A1', 'ArrivalTime')
        worksheet.write('B1', 'ItemName')
        worksheet.write('C1', 'Quantity')
        worksheet.write('D1', 'PO')
        worksheet.write('E1', 'WS1_target')
        worksheet.write('F1', 'WS1_real')
        worksheet.write('G1', 'WS2_target')
        worksheet.write('H1', 'WS2_real')
        worksheet.write('I1', 'WS3_target')
        worksheet.write('J1', 'WS3_real')
        worksheet.write('K1', 'WS4_target')
        worksheet.write('L1', 'WS4_real')
        worksheet.write('M1', 'SEQ')
        worksheet.write('N1', 'total')

        for i, order in enumerate(self.schedule):
            worksheet.write(i+1, 0, 0)
            worksheet.write(i+1, 1, "Product")
            worksheet.write(i+1, 2, 1)
            worksheet.write(i+1, 3, order)
            worksheet.write(i+1, 4, self.orders[order].ws1_count)
            worksheet.write(i+1, 5, 0)
            worksheet.write(i+1, 6, self.orders[order].ws2_count)
            worksheet.write(i+1, 7, 0)
            worksheet.write(i+1, 8, self.orders[order].ws3_count)
            worksheet.write(i+1, 9, 0)
            worksheet.write(i+1, 10, self.orders[order].ws4_count)
            worksheet.write(i+1, 11, 0)
            worksheet.write(i+1, 12, self.orders[order].seq)
            worksheet.write(i+1, 13, self.orders[order].ws1_count + self.orders[order].ws2_count + self.orders[order].ws3_count + self.orders[order].ws4_count)
        workbook.close()
        

