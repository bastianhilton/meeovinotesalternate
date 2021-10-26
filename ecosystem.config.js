module.exports = {
  "apps": [
    {
      "name": "meeovinotes",
      "cwd": "../alternatenotes",
      "args": ["runserver", "0.0.0.0:8086"], 
      "script": "manage.py",
      "exec_mode": "fork",
      "exec_interpreter": "python"
    },
    /*{
      "name": "graphqlmesh",
      "cwd": "../alternate-cms",
      "args": ["yarn", "mesh", "0.0.0.0:4000"],
      "script": "dev",
    }*/
  ]
}