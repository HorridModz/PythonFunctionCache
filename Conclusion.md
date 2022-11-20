# Conclusion

# Rankings

I ranked the best caches for speed, compactness, and customizability.

_Note: The difference in speed is trivial between **Default Argument Cache**, **Global Variable Cache**, and **Class Cache**. As functools is a wrapper for a library coded in c, the functools cache is much faster (as most standard libraries should be)._

Speed: 
1. Functools Cache
2. Default Argument Cache
3. Global Variable Cache
4. Class Cache

Compactness: 
1. Functools cache
2. Global Variable Cache
3. Default Argument Cache
4. Class Cache

Customizability: 
1. Global Variable Cache
2. Class Cache
3. Default Argument Cache
4. Functools Cache

# Verdict

Here are my recommendations for what cache suits what situation.

**Functools Cache** is great for caching the results of small functions. Due to its compactness, it is easy to implement and remove. This technique should be used if you want to quickly make some obvious, simple optimizations that will make your program much faster.

**Default Argument Cache** is necessary if you have a function that has more than one step, and you want to cache one (or more) of these steps. While functools cache only caches function input and output, this technique allows you to control exactly what is cached. However, the flexibility comes at the cost of boilerplate and speed.

**Class Cache** is the same as default argument cache, but it uses an object-oriented approach. Having your function - as well as its cache - in a class not only removes the function's default argument, but it allows you to reset the cache, or even store multiple caches at once. However, the boilerplate doesn't go away - you're just distributing it over a class instead of throwing it all into one function. In addition, you or someone else has to create an instance of the class just to use your function - which is annoying, especially considering how this class object has to be stored as a global variable or passed into all functions in order to maintain the cache. On top of all this, you have to come up with a name for the class - and if the class only has one function, the name will often be redundant.

**Global Variable Cache** is a much cleaner approach than the class cache. It has all the benefits, but almost all the cons are removed. You can still reset the cache, and since you can set the cache from outside, you can manage multiple caches in a list, file, another variable, or whatever other method you choose. In addition, since the cache is global, it goes both ways: Not only can you reset it, but you can load the cache from a file etc. on runtime. Though the function using the cache much have some boilerplate, much of it, such as the default argument, is gone. All these perks come with two downsides: First, the cache must be manually reset (or loaded) on initialization. Second, you add one variable to the global namespace - which can get messy when you have lots of functions using this caching technique.