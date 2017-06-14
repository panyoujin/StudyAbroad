from flask import Flask


app = Flask(__name__)
import  planner_project.api.user.register
import  planner_project.api.user.login
import  planner_project.api.home.index
import  planner_project.api.planner.planner