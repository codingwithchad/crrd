package com.cs419_group18.corvallisreuseandrepairdirectory;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Handler;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.TextView;

import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.MapFragment;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;
import com.loopj.android.http.AsyncHttpClient;
import com.loopj.android.http.JsonHttpResponseHandler;

import org.apache.http.Header;
import org.json.JSONArray;
import org.json.JSONObject;


public class RepairBizDetailActivity extends ActionBarActivity implements OnMapReadyCallback {
    TextView bizNameTextView;
    TextView bizAddressTextView;
    TextView bizCityTextView;
    TextView bizPhoneTextView;
    TextView bizHoursTextView;
    TextView bizWebsiteTextView;
    String name;
    double latitude = 0;
    double longitude = 0;
    private static final String BASE_URL = "http://52.26.111.76:8000/crrd/";
    AsyncHttpClient client = new AsyncHttpClient();
    String pk;      //DB primary key
    ProgressDialog progDialog;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_repair_biz_detail);

        bizNameTextView = (TextView) findViewById(R.id.repairBizName);
        bizAddressTextView = (TextView) findViewById(R.id.repairBizAddress);
        bizCityTextView = (TextView) findViewById(R.id.repairBizCity);
        bizPhoneTextView = (TextView) findViewById(R.id.repairBizPhone);
        bizHoursTextView = (TextView) findViewById(R.id.repairBizHours);
        bizWebsiteTextView = (TextView) findViewById(R.id.repairBizWebsite);

        MapFragment mapFragment = (MapFragment) getFragmentManager().findFragmentById(R.id.repairMap);
        mapFragment.getMapAsync(this);

        pk = this.getIntent().getExtras().getString("pk");

        progDialog = new ProgressDialog(this);
        progDialog.setMessage("Fetching data");
        progDialog.setCancelable(true);

        progDialog.show();

        // perform GET to do initial fill of the item listview
        client.get(BASE_URL + pk + "/repbusdetail/", new JsonHttpResponseHandler() {
            @Override
            public void onSuccess(int statusCode, Header[] headers, JSONArray response) {
                progDialog.dismiss();
                JSONObject item, fields;
                try {
                    item = response.getJSONObject(0);
                    fields = item.getJSONObject("fields");
                    name = fields.getString("busName");
                    bizNameTextView.setText(name);
                    bizAddressTextView.setText(fields.getString("address1"));
                    bizCityTextView.setText(fields.getString("city"));
                    bizPhoneTextView.setText(fields.getString("phone1"));
                    bizHoursTextView.setText(fields.getString("hours"));
                    bizWebsiteTextView.setText(fields.getString("web"));
                    latitude = fields.getDouble("latitude");
                    longitude = fields.getDouble("longitude");
                } catch (Exception ex) {
                    Log.d("jh json exception", ex.getMessage());
                }
            }

            @Override
            public void onFailure(int statusCode, Header[] headers, String responseString, Throwable error) {
                progDialog.dismiss();
                Log.d("jh item GET fail", responseString);
            }
        });
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_repair_biz_detail, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    @Override
    public void onMapReady(GoogleMap map) {
        final GoogleMap newMap = map;

        Handler handler = new Handler();
        handler.postDelayed(new Runnable() {
            @Override
            public void run() {
                if (latitude != 0 && longitude != 0) {
                    newMap.addMarker(new MarkerOptions()
                            .position(new LatLng(latitude, longitude))
                            .title(name));
                }
            }
        }, 3000);

        map.setOnMapClickListener(new GoogleMap.OnMapClickListener() {
            @Override
            public void onMapClick(LatLng latLng) {
                Intent intent = new Intent(RepairBizDetailActivity.this, RepairMapActivity.class);
                intent.putExtra("lat", latitude);
                intent.putExtra("lng", longitude);
                intent.putExtra("name", name);
                startActivity(intent);
            }
        });
    }
}
