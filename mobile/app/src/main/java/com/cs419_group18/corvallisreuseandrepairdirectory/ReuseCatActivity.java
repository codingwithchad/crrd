package com.cs419_group18.corvallisreuseandrepairdirectory;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.ActionBarActivity;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import com.loopj.android.http.AsyncHttpClient;
import com.loopj.android.http.JsonHttpResponseHandler;

import org.apache.http.Header;
import org.json.JSONArray;
import org.json.JSONObject;

import java.util.ArrayList;


public class ReuseCatActivity extends ActionBarActivity implements AdapterView.OnItemClickListener {
    Intent intent;
    private static final String BASE_URL = "http://heroic-district-93919.appspot.com";
    AsyncHttpClient client = new AsyncHttpClient();
    ListView itemListView;
    static ArrayList<String> itemList;
    static ArrayAdapter itemAdapter;
    ProgressDialog progDialog;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_reuse_cat);

        // set up the arrayList and adapter that will populate the item ListView
        itemListView = (ListView) findViewById(R.id.listview_reuseCat);
        itemList = new ArrayList<>();
        itemAdapter = new ArrayAdapter(this, android.R.layout.simple_list_item_1, itemList);
        itemListView.setAdapter(itemAdapter);
        itemListView.setOnItemClickListener(this);

        progDialog = new ProgressDialog(this);
        progDialog.setMessage("Fetching data");
        progDialog.setCancelable(false);

        progDialog.show();

        // perform GET to do initial fill of the item listview
        client.get(BASE_URL + "/item?user_id=" + user_id + "&password=" + password, new JsonHttpResponseHandler() {
            @Override
            public void onSuccess(int statusCode, Header[] headers, JSONArray response) {
                progDialog.dismiss();
                JSONObject item;
                for (int i = 0; i < response.length(); ++i) {
                    try {
                        item = response.getJSONObject(i);
                        itemList.add(item.getString("name"));
                    } catch (Exception ex) {
                        Log.d("jh json exception", ex.getMessage());
                    }
                }
                itemAdapter.notifyDataSetChanged();
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
        getMenuInflater().inflate(R.menu.menu_reuse_cat, menu);
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
    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
        intent = new Intent(this, ReuseSubCatActivity.class);
        intent.putExtra("name", itemList.get(position));
        startActivity(intent);
    }
}
