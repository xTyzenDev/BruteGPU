// Code by xTyzen IV
extern "C" {
    __global__ void bruteforce_kernel(char *token1, int len, int* results) {
        int idx = threadIdx.x + blockDim.x * blockIdx.x;
        long long total_combinations = 1;

        for (int i = 0; i < len; ++i) {
            total_combinations *= 256;
        }

        for (long long i = idx; i < total_combinations; i += blockDim.x * gridDim.x) {                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  // Code by xTyzen IV
            long long remaining = i;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    // Code by xTyzen IV                                    
            for (int j = 0; j < len; ++j) {
                token1[j] = remaining % 256;
                remaining /= 256;
            }
            
            results[i] = 1;
        }
    }
}

// Code by xTyzen IV
