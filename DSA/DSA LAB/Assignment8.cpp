#include <iostream>
using namespace std;

const int maxN = 100;
int totalComparisons = 0;  // Added counter

void merge(int a[], int l, int m, int r) {
    int i = l;      // Index for left subarray
    int j = m + 1;  // Index for right subarray
    int k = 0;      // Index for auxiliary array
    static int aux[maxN];
    
    // Merge the two halves into auxiliary array
    while (i <= m && j <= r) {
        totalComparisons++;  // Increment counter
        cout << "Comparing " << a[i] << " and " << a[j] << endl;
        if (a[i] <= a[j]) {
            aux[k++] = a[i++];
        } else {
            aux[k++] = a[j++];
        }
    }
    
    // Copy remaining elements from left half
    while (i <= m) {
        aux[k++] = a[i++];
    }
    
    // Copy remaining elements from right half
    while (j <= r) {
        aux[k++] = a[j++];
    }
    
    // Copy back to original array
    for (i = 0; i < k; i++) {
        a[l + i] = aux[i];
    }
}

void mergesort(int a[], int l, int r) {
    if (r <= l) return;
    int m = (r+l)/2;
    mergesort(a, l, m);    // Sort first half
    mergesort(a, m+1, r);  // Sort second half
    merge(a, l, m, r);     // Merge the halves
}

int main() {
    int arr[] = {8, 3, 1, 2, 4, 6, 5, 7};
    int n = 8;
    
    cout << "Before sorting: ";
    for(int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << "\n\n";
    
    totalComparisons = 0;  // Reset counter
    mergesort(arr, 0, n-1);
    
    cout << "\nAfter sorting: ";
    for(int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
    
    cout << "\nTotal number of comparisons: " << totalComparisons << endl;
    return 0;
}
