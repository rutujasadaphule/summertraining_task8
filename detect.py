{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "signal-layout",
   "metadata": {},
   "outputs": [],
   "source": [
    "#!/usr/bin/python3\n",
    "\n",
    "import cgi\n",
    "import subprocess\n",
    "import requests\n",
    "import xmltodict\n",
    "import json\n",
    "\n",
    "print(\"content-type: text/html\")\n",
    "print()\n",
    "\n",
    "f = cgi.FieldStorage()\n",
    "\n",
    "plate_no = f.getvalue(\"Number\")\n",
    "r = requests.get(\"http://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber={0}&username=username\".format(str(plate_no)))\n",
    "\n",
    "data = xmltodict.parse(r.content)\n",
    "jdata = json.dumps(data)\n",
    "df = json.loads(jdata)\n",
    "df1 = json.loads(df['Vehicle']['vehicleJson'])\n",
    "print(\"Description     : \",df1[\"Description\"])\n",
    "print(\"RegistrationDate: \",df1[\"RegistrationDate\"])\n",
    "print(\"Location        : \",df1[\"Location\"])\n",
    "print(\"NumberOfSeats   : \",df1[\"NumberOfSeats\"][\"CurrentTextValue\"])\n",
    "print(\"VehicleIdentificationNumber: \",df1[\"VechileIdentificationNumber\"])\n",
    "print(\"EngineNumber    : \",df1[\"EngineNumber\"])\n",
    "print(\"EngineSize      : \",df1[\"EngineSize\"][\"CurrentTextValue\"])\n",
    "print(\"FuelType        : \",df1[\"FuelType\"][\"CurrentTextValue\"])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
