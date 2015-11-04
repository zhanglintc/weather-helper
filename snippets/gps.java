LocationManager locMgr = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
Location location = locMgr.getLastKnownLocation(LocationManager.NETWORK_PROVIDER);
double lng = location.getLongitude();
Log.i("gps", String.valueOf(lng));