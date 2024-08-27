import csv
import io
from os import path
from shutil import make_archive

import xlsxwriter
# Geodjango point geometries
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from observations.models import Category1, Category2, Category3, Category4


# Photo download
@login_required(login_url='/accounts/login')
def download_category1_photo(request, file_name="category1"):
    if request.method == 'GET':
        month = request.GET.get('month')
        year = request.GET.get('year')
        file_path = "/media/photos/" + file_name + "/" + str(year) + "/" + str(month)
        file_path2 = "media/photos/" + file_name + "/" + str(year) + "/" + str(month)
        if path.exists(file_path2):
            make_archive(file_path2, "zip", file_path2)
            response = HttpResponse(status=200)
            response['Content-Type'] = ''
            response['Content-Disposition'] = 'attachment; filename="category1.zip"'
            response['X-Accel-Redirect'] = file_path + '.zip'
            return response
        else:
            messages.info(request, 'No pictures. Please try another selection.')
            return redirect("/downloads/")


@login_required(login_url='/accounts/login')
def download_category2_photo(request, file_name="category2"):
    if request.method == 'GET':
        month = request.GET.get('month')
        year = request.GET.get('year')
        file_path = "/media/photos/" + file_name + "/" + str(year) + "/" + str(month)
        file_path2 = "media/photos/" + file_name + "/" + str(year) + "/" + str(month)
        if path.exists(file_path2):
            make_archive(file_path2, "zip", file_path2)
            response = HttpResponse (status=200)
            response['Content-Type'] = ''
            response['Content-Disposition'] = 'attachment; filename="category2.zip"'
            response['X-Accel-Redirect'] = file_path + '.zip'
            return response
        else:
            messages.info(request, 'No pictures. Please try another selection.')
            return redirect("/downloads/")


@login_required(login_url='/accounts/login')
def download_category3_photo(request, file_name="category3"):
    if request.method == 'GET':
        month = request.GET.get('month')
        year = request.GET.get('year')
        file_path = "/media/photos/" + file_name + "/" + str(year) + "/" + str(month)
        file_path2 = "media/photos/" + file_name + "/" + str(year) + "/" + str(month)
        if path.exists(file_path2):
            make_archive(file_path2, "zip", file_path2)
            response = HttpResponse(status=200)
            response['Content-Type'] = ''
            response['Content-Disposition'] = 'attachment; filename="category3.zip"'
            response['X-Accel-Redirect'] = file_path + '.zip'
            return response
        else:
            messages.info(request, 'No pictures. Please try another selection.')
            return redirect("/downloads/")


@login_required(login_url='/accounts/login')
def download_category4_photo(request, file_name="category4"):
    if request.method == 'GET':
        month = request.GET.get('month')
        year = request.GET.get('year')
        file_path = "/media/photos/" + file_name + "/" + str(year) + "/" + str(month)
        file_path2 = "media/photos/" + file_name + "/" + str(year) + "/" + str(month)
        if path.exists(file_path2):
            make_archive(file_path2, "zip", file_path2)
            response = HttpResponse (status=200)
            response['Content-Type'] = ''
            response['Content-Disposition'] = 'attachment; filename="category4.zip"'
            response['X-Accel-Redirect'] = file_path + '.zip'
            return response
        else:
            messages.info(request, 'No pictures. Please try another selection.')
            return redirect("/downloads/")


@login_required(login_url='/accounts/login')
def download_category1(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="category1s.csv"'
    writer = csv.writer(response)
    writer.writerow(
        ['ID', 'Creator', 'Title', 'Publisher', 'PublicationYear', 'Subject', 'ResourceType', 'License',
         'DateFirstCreated', 'DateLastUpdated', 'Category1Subject', 'Certainty', 'Number', 'Category1Feature1',
         'Category1Feature2', 'Category1Feature3', 'Latitude', 'Longitude', 'Position', 'AccuracyGPS',
         'ObservationDate',
         'ObservationTime', 'Photo'])
    category1s = Category1.objects.filter(Flag=None).values_list('id', 'Creator', 'Title', 'Publisher',
                                                                  'PublicationYear', 'Subject', 'ResourceType',
                                                                  'License', 'DateFirstCreated', 'DateLastUpdated',
                                                                  'Category1Subject', 'Certainty', 'Number', 'Category1Feature1',
                                                                    'Category1Feature2', 'Category1Feature3',
                                                                  'Lat', 'Lon', 'Position', 'AccuracyGPS',
                                                                  'ObservationDate',
                                                                  'ObservationTime', 'Photo')
    for category1 in category1s:
        writer.writerow(category1)
    return response


@login_required(login_url='/accounts/login')
def download_category1_xlsx(request):
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {'remove_timezone': True})
    worksheet = workbook.add_worksheet()

    header = ['ID', 'Creator', 'Title', 'Publisher', 'PublicationYear', 'Subject', 'ResourceType', 'License',
              'DateFirstCreated', 'DateLastUpdated', 'Category1Subject', 'Certainty', 'Number', 'Category1Feature1', 'Category1Feature2',
              'Category1Feature3', 'Latitude', 'Longitude', 'Position', 'AccuracyGPS', 'ObservationDate',
              'ObservationTime', 'Photo']

    category1s = Category1.objects.filter(Flag=None).values_list('id', 'Creator', 'Title', 'Publisher',
                                                                  'PublicationYear', 'Subject', 'ResourceType',
                                                                  'License',
                                                                  'DateFirstCreated', 'DateLastUpdated',
                                                                  'Category1Subject',
                                                                  'Certainty', 'Number', 'Category1Feature1', 'Category1Feature2',
                                                                  'Category1Feature3', 'Lat', 'Lon', 'Position',
                                                                  'AccuracyGPS',
                                                                  'ObservationDate', 'ObservationTime', 'Photo'
                                                                  )
    data = header
    for col_num, cell_data in enumerate(data):
        worksheet.write(0, col_num, cell_data)
    for row_num, columns in enumerate(category1s):
        for col_num, cell_data in enumerate(columns):
            worksheet.write(row_num + 1, col_num, cell_data)

        # Close the workbook before sending the data.
    workbook.close()

    # Rewind the buffer.
    output.seek(0)

    # Set up the Http response.
    filename = 'category1.xlsx'
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response


@login_required(login_url='/accounts/login')
def download_category2(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="category2.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Creator', 'Title', 'Publisher', 'PublicationYear', 'Subject', 'ResourceType', 'License',
                     'DateFirstCreated', 'DateLastUpdated',
                     'Category2Subject', 'Certainty', 'Category2Feature1', 'Category2Feature2',
                     'Category2Feature3', 'Category2Feature4', 'Category2Feature5', 'Category2Feature6',
                     'Category2Feature7', 'Category2Feature8',
                     'Latitude', 'Longitude', 'Position', 'AccuracyGPS', 'ObservationDate', 'Photo'])
    category2s = Category2.objects.filter(Flag=None).values_list('id', 'Creator', 'Title',
                                                                                            'Publisher',
                                                                                            'PublicationYear',
                                                                                            'Subject', 'ResourceType',
                                                                                            'License',
                                                                                            'DateFirstCreated',
                                                                                            'DateLastUpdated',
                                                                                            'Category2Subject', 'Certainty',
                                                                                            'Category2Feature1',
                                                                                            'Category2Feature2',
                                                                                            'Category2Feature3', 'Category2Feature4',
                                                                                            'Category2Feature5', 'Category2Feature6',
                                                                                            'Category2Feature7',
                                                                                            'Category2Feature8',
                                                                                            'Lat', 'Lon', 'Position',
                                                                                            'AccuracyGPS',
                                                                                            'ObservationDate', 'Photo')
    for category2 in category2s:
        writer.writerow(category2)
    return response


@login_required(login_url='/accounts/login')
def download_category2_xlsx(request):
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {'remove_timezone': True})
    worksheet = workbook.add_worksheet()

    header = ['ID', 'Creator', 'Title', 'Publisher', 'PublicationYear', 'Subject', 'ResourceType', 'License',
              'DateFirstCreated', 'DateLastUpdated',
              'Category2Subject', 'Certainty', 'Category2Feature1', 'Category2Feature2',
              'Category2Feature3', 'Category2Feature4', 'Category2Feature5', 'Category2Feature6', 'Category2Feature7', 'Category2Feature8',
              'Latitude', 'Longitude', 'Position', 'AccuracyGPS', 'ObservationDate', 'Photo']

    category2s = Category2.objects.filter(Flag=None).values_list('id', 'Creator', 'Title',
                                                                                       'Publisher',
                                                                                       'PublicationYear',
                                                                                       'Subject', 'ResourceType',
                                                                                       'License',
                                                                                       'DateFirstCreated',
                                                                                       'DateLastUpdated',
                                                                                       'Category2Subject', 'Certainty',
                                                                                       'Category2Feature1',
                                                                                       'Category2Feature2',
                                                                                       'Category2Feature3', 'Category2Feature4',
                                                                                       'Category2Feature5', 'Category2Feature6',
                                                                                       'Category2Feature7',
                                                                                       'Category2Feature8',
                                                                                       'Lat', 'Lon', 'Position',
                                                                                       'AccuracyGPS',
                                                                                       'ObservationDate', 'Photo')
    data = header
    for col_num, cell_data in enumerate(data):
        worksheet.write(0, col_num, cell_data)
    for row_num, columns in enumerate(category2s):
        for col_num, cell_data in enumerate(columns):
            worksheet.write(row_num + 1, col_num, cell_data)

        # Close the workbook before sending the data.
    workbook.close()

    # Rewind the buffer.
    output.seek(0)

    # Set up the Http response.
    filename = 'category2.xlsx'
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response


# CSV download
@login_required(login_url='/accounts/login')
def download_category3(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="category3.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Creator', 'Title', 'Publisher', 'PublicationYear', 'Subject', 'ResourceType', 'License',
                     'DateFirstCreated', 'DateLastUpdated', 'Category3Subject', 'Certainty', 'Category3Feature1',
                     'Latitude', 'Longitude', 'Position', 'AccuracyGPS', 'Category3Feature2', 'ObservationDate', 'Photo'])
    category3s = Category3.objects.filter(Flag=None).values_list('id', 'Creator', 'Title', 'Publisher', 'PublicationYear',
                                                            'Subject', 'ResourceType', 'License', 'DateFirstCreated',
                                                            'DateLastUpdated', 'Category3Subject', 'Certainty', 'Category3Feature1',
                                                            'Lat', 'Lon', 'Position', 'AccuracyGPS', 'Category3Feature2',
                                                            'ObservationDate', 'Photo')
    for category3 in category3s:
        writer.writerow(category3)
    return response


@login_required(login_url='/accounts/login')
def download_category3_xlsx(request):
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {'remove_timezone': True})
    worksheet = workbook.add_worksheet()

    header = ['ID', 'Creator', 'Title', 'Publisher', 'PublicationYear', 'Subject', 'ResourceType', 'License',
              'DateFirstCreated', 'DateLastUpdated', 'Category3Subject', 'Certainty', 'Category3Feature1',
              'Latitude', 'Longitude', 'Position', 'AccuracyGPS', 'Category3Feature2', 'ObservationDate', 'Photo']

    category3s = Category3.objects.filter(Flag=None).values_list('id', 'Creator', 'Title', 'Publisher', 'PublicationYear',
                                                            'Subject', 'ResourceType', 'License', 'DateFirstCreated',
                                                            'DateLastUpdated', 'Category3Subject', 'Certainty',
                                                            'Category3Feature1',
                                                            'Lat', 'Lon', 'Position', 'AccuracyGPS', 'Category3Feature2',
                                                            'ObservationDate', 'Photo')
    data = header
    for col_num, cell_data in enumerate(data):
        worksheet.write(0, col_num, cell_data)
    for row_num, columns in enumerate(category3s):
        for col_num, cell_data in enumerate(columns):
            worksheet.write(row_num + 1, col_num, cell_data)

        # Close the workbook before sending the data.
    workbook.close()

    # Rewind the buffer.
    output.seek(0)

    # Set up the Http response.
    filename = 'category3.xlsx'
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response


@login_required(login_url='/accounts/login')
def download_category4(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="category4.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Creator', 'Title', 'Publisher', 'PublicationYear', 'Subject', 'ResourceType', 'License',
                     'DateFirstCreated', 'DateLastUpdated', 'Category4Subject', 'Certainty', 'Category4Feature1', 'Category4Feature2',
                     'Category4Feature3', 'Latitude', 'Longitude', 'Position', 'AccuracyGPS', 'ObservationDate', 'Photo'])
    category4s = Category4.objects.filter(Flag=None).values_list('id', 'Creator', 'Title',
                                                                                        'Publisher', 'PublicationYear',
                                                                                        'Subject', 'ResourceType',
                                                                                        'License', 'DateFirstCreated',
                                                                                        'DateLastUpdated', 'Category4Subject',
                                                                                        'Certainty', 'Category4Feature1',
                                                                                        'Category4Feature2', 'Category4Feature3',
                                                                                        'Lat', 'Lon', 'Position',
                                                                                        'AccuracyGPS',
                                                                                        'ObservationDate', 'Photo')
    for category4 in category4s:
        writer.writerow(category4)
    return response


@login_required(login_url='/accounts/login')
def download_category4_xlsx(request):
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {'remove_timezone': True})
    worksheet = workbook.add_worksheet()

    header = ['ID', 'Creator', 'Title', 'Publisher', 'PublicationYear', 'Subject', 'ResourceType', 'License',
              'DateFirstCreated', 'DateLastUpdated', 'Category4Subject', 'Certainty', 'Category4Feature1', 'Category4Feature2',
              'Category4Feature3', 'Latitude', 'Longitude', 'Position', 'AccuracyGPS', 'ObservationDate', 'Photo']

    category4s = Category4.objects.filter(Flag=None).values_list('id', 'Creator', 'Title',
                                                                                    'Publisher', 'PublicationYear',
                                                                                    'Subject', 'ResourceType',
                                                                                    'License', 'DateFirstCreated',
                                                                                    'DateLastUpdated', 'Category4Subject',
                                                                                    'Certainty', 'Category4Feature1',
                                                                                    'Category4Feature2', 'Category4Feature3',
                                                                                    'Lat', 'Lon', 'Position',
                                                                                    'AccuracyGPS',
                                                                                    'ObservationDate', 'Photo')
    data = header
    for col_num, cell_data in enumerate(data):
        worksheet.write(0, col_num, cell_data)
    for row_num, columns in enumerate(category4s):
        for col_num, cell_data in enumerate(columns):
            worksheet.write(row_num + 1, col_num, cell_data)

        # Close the workbook before sending the data.
    workbook.close()

    # Rewind the buffer.
    output.seek(0)

    # Set up the Http response.
    filename = 'category4.xlsx'
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response
