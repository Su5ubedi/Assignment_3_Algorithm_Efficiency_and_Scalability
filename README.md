Algorithm Efficiency and Scalability
This repository contains Python implementations and analyses for Randomized Quicksort and Hashing with Chaining. The first file is randomized_quicksort_analysis.py, which implements randomized and deterministic quicksort and then compares the performance of the two on different types of arrays and sizes. The script also plots the runtime comparison plots. The second file is the hash_table_chaining.py, which has been used to implement a hash table using chaining for collision resolution. 
How to Run
To run the scripts, you need to ensure that all the required dependencies have been installed. For example, "pip install matplotlib" can be used to install this library as it is required when plotting the runtime comparison plots. After installation, the two scripts can be executed directly. 
Results
Randomized Quicksort shows O(n log n) average-case performance, while the hash table shows efficient O(1 + alpha) operations with collision handling.

randomized_quicksort_analysis.py results
Analyzing Random arrays...
  Testing array of size 10...
    Randomized: 0.0011s, Deterministic: 0.0000s
  Testing array of size 50...
    Randomized: 0.0027s, Deterministic: 0.0000s
  Testing array of size 100...
    Randomized: 0.0041s, Deterministic: 0.0010s
  Testing array of size 500...
    Randomized: 0.0129s, Deterministic: 0.0070s
  Testing array of size 1000...
    Randomized: 0.0224s, Deterministic: 0.0156s

Analyzing Sorted arrays...
  Testing array of size 10...
    Randomized: 0.0000s, Deterministic: 0.0000s
  Testing array of size 50...
    Randomized: 0.0000s, Deterministic: 0.0000s
  Testing array of size 100...
    Randomized: 0.0000s, Deterministic: 0.0156s
  Testing array of size 500...
    Randomized: 0.0156s, Deterministic: 0.1719s
  Testing array of size 1000...
    Randomized: 0.0313s, Deterministic: 0.7695s

Analyzing Reverse-Sorted arrays...
  Testing array of size 10...
    Randomized: 0.0000s, Deterministic: 0.0000s
  Testing array of size 50...
    Randomized: 0.0156s, Deterministic: 0.0000s
  Testing array of size 100...
    Randomized: 0.0000s, Deterministic: 0.0000s
  Testing array of size 500...
    Randomized: 0.0156s, Deterministic: 0.1094s
  Testing array of size 1000...
    Randomized: 0.0313s, Deterministic: 0.4841s

Analyzing Repeated-Elements arrays...
  Testing array of size 10...
    Randomized: 0.0000s, Deterministic: 0.0000s
  Testing array of size 50...
    Randomized: 0.0000s, Deterministic: 0.0000s
  Testing array of size 100...
    Randomized: 0.0000s, Deterministic: 0.0000s
  Testing array of size 500...
    Randomized: 0.0313s, Deterministic: 0.0313s
  Testing array of size 1000...
    Randomized: 0.0937s, Deterministic: 0.0781s

Performance Results:
Random Array | Size: 10 | Randomized: 0.0011s | Deterministic: 0.0000s
Random Array | Size: 50 | Randomized: 0.0027s | Deterministic: 0.0000s
Random Array | Size: 100 | Randomized: 0.0041s | Deterministic: 0.0010s
Random Array | Size: 500 | Randomized: 0.0129s | Deterministic: 0.0070s
Random Array | Size: 1000 | Randomized: 0.0224s | Deterministic: 0.0156s
Sorted Array | Size: 10 | Randomized: 0.0000s | Deterministic: 0.0000s
Sorted Array | Size: 50 | Randomized: 0.0000s | Deterministic: 0.0000s
Sorted Array | Size: 100 | Randomized: 0.0000s | Deterministic: 0.0156s
Sorted Array | Size: 500 | Randomized: 0.0156s | Deterministic: 0.1719s
Sorted Array | Size: 1000 | Randomized: 0.0313s | Deterministic: 0.7695s
Reverse-Sorted Array | Size: 10 | Randomized: 0.0000s | Deterministic: 0.0000s
Reverse-Sorted Array | Size: 50 | Randomized: 0.0156s | Deterministic: 0.0000s
Reverse-Sorted Array | Size: 100 | Randomized: 0.0000s | Deterministic: 0.0000s
Reverse-Sorted Array | Size: 500 | Randomized: 0.0156s | Deterministic: 0.1094s
Reverse-Sorted Array | Size: 1000 | Randomized: 0.0313s | Deterministic: 0.4841s
Repeated-Elements Array | Size: 10 | Randomized: 0.0000s | Deterministic: 0.0000s
Repeated-Elements Array | Size: 50 | Randomized: 0.0000s | Deterministic: 0.0000s
Repeated-Elements Array | Size: 100 | Randomized: 0.0000s | Deterministic: 0.0000s
Repeated-Elements Array | Size: 500 | Randomized: 0.0313s | Deterministic: 0.0313s
Repeated-Elements Array | Size: 1000 | Randomized: 0.0937s | Deterministic: 0.0781s


hash_table_chaining.py results
Inserting key-value pairs...
Testing search operation...
Search key0: 0
Search key1: 2
Search key2: 4
Search key3: 6
Search key4: 8
Search key5: 10
Search key6: 12
Search key7: 14
Search key8: 16
Search key9: 18
Search key10: 20
Search key11: 22
Search key12: 24
Search key13: 26
Search key14: 28
Search key15: 30
Search key16: 32
Search key17: 34
Search key18: 36
Search key19: 38
Search key20: 40
Search key21: 42
Search key22: 44
Search key23: 46
Search key24: 48
Search key25: 50
Search key26: 52
Search key27: 54
Search key28: 56
Search key29: 58
Search key30: 60
Search key31: 62
Search key32: 64
Search key33: 66
Search key34: 68
Search key35: 70
Search key36: 72
Search key37: 74
Search key38: 76
Search key39: 78
Search key40: 80
Search key41: 82
Search key42: 84
Search key43: 86
Search key44: 88
Search key45: 90
Search key46: 92
Search key47: 94
Search key48: 96
Search key49: 98
Deleting some keys...
Re-testing search after deletion...
Search key0: None
Search key1: None
Search key2: None
Search key3: None
Search key4: None
Search key5: None
Search key6: None
Search key7: None
Search key8: None
Search key9: None
Hash table operation completed.
