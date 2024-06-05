#include <stdio.h>
#include <iostream>
#include <stdlib.h>

using namespace std;
int a[1005], b[1005], dp[1005][1005];
int main(){
    int n, m;
    cin >> n >> m;
    for(int i = 1;i <= n;i++) cin >> a[i];
    for(int i = 1;i <= m;i++) cin >> b[i];
	
    int ans = INT_MIN;
    for(int i = 1;i <= n;i++){
        for(int j = 1;j <= m;j++){
            dp[i][j] = max(dp[i-1][j-1] + a[i] * b[j], a[i] * b[j]);
            cout << dp[i][j] << endl;
            ans = max(ans, dp[i][j]);
	    }
    }
	
    reverse(b+1, b+1+m);

    memset(dp, 0, sizeof(dp));
    for(int i = 1;i <= n;i++){
	    for(int j = 1;j <= m;j++){
	        dp[i][j] = max(dp[i-1][j-1] + a[i] * b[j], a[i] * b[j]);
            cout << dp[i][j] << endl;
	        ans = max(ans, dp[i][j]);
	    }
    }
	
    cout << ans << '\n';
}