__kernel void calc_pixel(__global float* image,const float acorn, const float bcorn, const float size,const int width){
    int i = get_global_id(0);
    int j = get_global_id(1);

    int count = 0;
    //real and imaginary parts of c
    float ca = acorn + i*size/width;
    float cb = bcorn + j*size/width;

    //Real and imaginary parts of z
    float zx = 0;
    float zy = 0;

    float xtemp =0;
    //iterate 100 times to check if the orbit is bounded
    while(count < 100 && (zx*zx + zy*zy <4)){
        count = count+1;
        xtemp = zx*zx - zy*zy;
        zy = 2*zx*zy +cb;
        zx= xtemp + ca;
    }
    if(count == 100){
        image[j* width + i] = 1;
    }
    else{
        image[j* width + i] = count;
    }
    image[j* width + i] = count;
}