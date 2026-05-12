from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import CountryAnalyser


fm = FileManager('students.csv')

if not fm.check_file():
    print("Stopping program.")
    exit()

fm.create_output_folder()

dl = DataLoader('students.csv')
dl.load()
dl.preview()

analyser = CountryAnalyser(dl.students)

print(analyser)

analyser.analyse()
analyser.print_results()

saver = ResultSaver(
    analyser.result,
    'output/result.json'
)

report = Report(analyser, saver)

report.generate()