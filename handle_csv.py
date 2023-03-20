from datetime import datetime
import update_cell_color as up_color
import share_file


def send_mail(data, file_ids_dic, SPREADSHEET_ID, SHEET_NAME):
    # Processing required information
    row_size = data.shape[0]
    column_size = data.shape[1]

    # Start to send email
    for row in range(row_size):
        # person's mail
        gmail = data.at[row, "電子郵件地址"]
        print(row, gmail)
        # How many days need to send
        file_ids = []
        offset = -2
        max_date = " "
        for column in range(5, column_size):
            date = data.iat[row, column]
            if date == today_str:
                if file_ids_dic.get(column):

                    # print("row: ", row, "col: ", column)  # test
                    red, green, blue = up_color.get_cell_color(row + 1, column, SPREADSHEET_ID)

                    if (red, green, blue) == (1, 1, 1):  # if cell's color is white
                        file_ids.append(file_ids_dic.get(column))
                        offset += 2
                        up_color.update_cell_color(row + 1, column, 1, 1, 0, SPREADSHEET_ID, SHEET_NAME)  # yellow

                    elif (red, green, blue) == (1, 1, 0):  # if cell's color is yellow
                        file_ids.append(file_ids_dic.get(column))
                        offset += 2
                        up_color.update_cell_color(row + 1, column, 0, 1, 0, SPREADSHEET_ID, SHEET_NAME)  # green

                    elif (red, green, blue) == (0, 1, 0):  # if cell's color is green
                        max_date = max_date + data.columns[column] + " "
                        file_ids.append(file_ids_dic.get(column))
                        offset += 2
                        up_color.update_cell_color(row + 1, column, 0, 1, 1, SPREADSHEET_ID, SHEET_NAME)  # blue

        print(file_ids, offset)
        if offset != -2:
            for file_id in file_ids:
                share_file.share_file(file_id, gmail, offset, max_date)


# Get time
this_month = datetime.now().month
today = datetime.now().day
today_str = str(this_month) + "/" + str(today)
