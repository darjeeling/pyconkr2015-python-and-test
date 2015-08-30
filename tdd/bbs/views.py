# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os.path
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, FormView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse


def test_view(request):
    return render(request, 'test.html')
