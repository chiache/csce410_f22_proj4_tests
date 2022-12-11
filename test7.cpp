#include <stdio.h>
#include <unistd.h>
#include "uthread.h"

void long_thread(void* arg)
{
    usleep(1000000);
    uthread_exit();
}

void thread1(void* arg)
{
    uthread_set_param(5);
    for (int i = 0; i < 10; i++) {
        printf("This is thread 1\n");
        uthread_yield();
    }
    uthread_exit();
}

void thread2(void* arg)
{
    for (int i = 0; i < 10; i++) {
        printf("This is thread 2\n");
	uthread_set_param(i + 1);
        uthread_yield();
    }
    uthread_exit();
}

void thread3(void* arg)
{
    for (int i = 0; i < 10; i++) {
        printf("This is thread 3\n");
	uthread_set_param(10 - i);
        uthread_yield();
    }
    uthread_exit();
}

int main(int argc, const char** argv)
{
    uthread_set_policy(UTHREAD_PRIORITY);
    uthread_init();
    uthread_create(long_thread, NULL);
    uthread_create(long_thread, NULL);
    uthread_create(long_thread, NULL);
    uthread_create(thread1, NULL);
    uthread_create(thread2, NULL);
    uthread_create(thread3, NULL);
    uthread_cleanup();
    return 0;
}
