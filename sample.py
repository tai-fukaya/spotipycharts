import spotipycharts as sc

charts = sc.Spotipycharts()
# get country code
country_list = charts.get_country_list()
country_code = country_list[0].get('code')
print(country_list[0])
# get duration code
duration_list = charts.get_duration_list(sc.ChartType.VIRAL, country_code, sc.FrequencyType.WEEKLY)
duration_list = charts.viral.weekly.get_duration_list(country_code)
duration_code = duration_list[0].get('code')
print(duration_list[0])
# download csv
chart_csv = charts.download_csv(sc.ChartType.VIRAL, country_code, sc.FrequencyType.WEEKLY, duration_code)
chart_csv = charts.viral.weekly.download_csv(country_code, duration_code)
print(chart_csv)
# csv to list
chart_item_list = sc.util.csv_to_list(chart_csv)
print(len(chart_item_list))
print(chart_item_list[0])
