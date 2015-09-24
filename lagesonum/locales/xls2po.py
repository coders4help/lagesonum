# encoding = "utf8'

# script to create several .po files in subdirectories from an excel table
# accepted languages are taken from bottle main file
# .po files still need compilation with msgfmt afterwards for translations to take effect

__author__ = 'f.zesch'

import xlrd

# PARAMETERS

WB_NAME = "Translations.xlsx"
KEY = "Key"
ID_S = "msgid"
STR_S = "msgstr"
WRAP_LEN = 66
KEY_COL = 0
DESC_COL = 1
EOL_STR = "\n"

def wrap_string(s):
    """
    Returns a wrapped string suitable for multiline msgstr in .po files
    :param s:
    :return:
    """

    if len(s) > WRAP_LEN:
        wrapped = []
        window = 0

        for _ in range(0,len(s),WRAP_LEN):

            wrapped.append('"'+s[window:window+WRAP_LEN]+'"')
            window += WRAP_LEN


        return wrapped
    else:
        return s

def write_po(sheet, col_nr, i18n_code, path=""):
    """
    write a .po file for a given language from excel sheet
    :param sheet:
    :param col_nr:
    :param i18n_code:
    :return:
    """

    with open(path+i18n_code+".po", encoding="utf8", mode="w") as po:

        #write header
        po.write("""msgid ""
        msgstr ""
        "Project-Id-Version: lagesonum"
        "Report-Msgid-Bugs-To:"
        "POT-Creation-Date: 2015-09-21 12:26+0200"
        "PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE"
        "Last-Translator:"
        "Language-Team: LANGUAGE <LL@li.org>"
        "MIME-Version: 1.0"
        "Content-Type: text/plain; charset=UTF-8"
        "Content-Transfer-Encoding: 8bit"
        """)

        po.write("\n\n")

        for row in range(1,sheet.nrows):

            # write description
            po.write("#: " + str(sheet.cell(row, DESC_COL).value)+EOL_STR)

            # write msgid
            po.write(ID_S + ' "' + str(sheet.cell(row, KEY_COL).value)+'"'+EOL_STR)

            # write msgstr
            wrapped_msgstr = wrap_string(sheet.cell(row, col_nr).value)

            if len ("".join(wrapped_msgstr)) < WRAP_LEN:
                po.write(STR_S + ' "' + wrapped_msgstr + '"' + EOL_STR)
            else:
                po.write(STR_S + ' ""' + EOL_STR)

                for msgstr_line in wrapped_msgstr:
                    po.write( msgstr_line + EOL_STR)

            po.write("\n")

def get_lang_cols(i18n_sheet):
    """
    finds the column numbers for given translations
    :param i18n_sheet:
    :return:
    """
    lang_dict = {}
    for col in range(0,i18n_sheet.ncols):

        xl_title = str(i18n_sheet.cell(0,col).value)

        if xl_title in langs:
            lang_dict[xl_title] = col

    return lang_dict


################################################################################

if __name__ == "__main__":

    # languages for which .po-files will be created
    from lagesonum.bottle_app import LANGS
    langs =[l for l,_ in LANGS]

    # open excel sheet
    wb = xlrd.open_workbook(WB_NAME)
    i18n_sheet = wb.sheet_by_index(0)

    # read columns where translations can be found
    lang_cols = get_lang_cols(i18n_sheet)

    # write .po files
    for loc in lang_cols:
        write_po(i18n_sheet, lang_cols[loc], i18n_code=loc, path=loc+"/LC_MESSAGES/")

    #todo: compile .po files to .mo files with msgfmt