#include <stdio.h>
#include <unistd.h>
#include "uthread.h"

void thread1(void* arg)
{
    for (int i = 0; i < 10; i++) {
        fprintf(stderr, "This is thread 1\n");
        usleep(1000);
    }
    uthread_exit();
}

void thread2(void* arg)
{
    for (int i = 0; i < 10; i++) {
        fprintf(stderr, "This is thread 2\n");
        usleep(1000);
    }
    uthread_exit();
}

int main(int argc, const char** argv)
{
    uthread_set_policy(UTHREAD_DIRECT_PTHREAD);
    uthread_init();
    uthread_create(thread1, NULL);
    uthread_create(thread2, NULL);
    uthread_cleanup();
    return 0;
}
